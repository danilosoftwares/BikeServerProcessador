from flask import jsonify
import tabelas
import banco
import time

def processar_all():
    processar_person()
    processar_customer()
    processar_product()
    processar_SalesOrderHeader()
    processar_SalesOrderDetail()
    processar_SpecialOfferProduct()
    return jsonify({"status":0,"retorno":"ok"}) 

def processar_person():                
    return jsonify(Gravador('person.person.csv',tabelas.Person, 1000)) 

def processar_customer():        
    return jsonify(Gravador('Sales.Customer.csv',tabelas.Customer, 1000)) 

def processar_SalesOrderHeader():    
    return jsonify(Gravador('Sales.SalesOrderHeader.csv',tabelas.SalesOrderHeader, 300)) 

def processar_SalesOrderDetail():    
    return jsonify(Gravador('Sales.SalesOrderDetail.csv',tabelas.SalesOrderDetail, 300)) 

def processar_SpecialOfferProduct():    
    return jsonify(Gravador('Sales.SpecialOfferProduct.csv',tabelas.SpecialOfferProduct, 1000)) 

def processar_product():    
    return jsonify(Gravador('Production.Product.csv',tabelas.Product, 1000))       


def Gravador(file, classe, bloco): 
    try:    
        retorno = {"status":0,"retorno":"ok"}   
        total = 0
        contador = 0
        wr = ''
        connector = banco.GetConnector()
        listaSQL = []
        i = 1
        while(i < len(file)):
            line = file[i].replace('\n','')
            if (line != ''):
                obj = classe(FormatNull(line.split(';')))
                if (wr == ''):
                    wr = obj.WhereSQL()
                if (len(listaSQL) == 0):
                    listaSQL.append('INSERT INTO '+type(obj).__name__+' ('+obj.Colunas+') ')
                    listaSQL.append('SELECT * FROM ( ')   
                else:
                    listaSQL.append('UNION ALL ')    
                listaSQL.append("SELECT "+obj.Valores+" FROM DUAL ")
                contador = contador + 1

            if (contador > bloco):
                listaSQL.append(') TB ')   
                listaSQL.append(wr)  
                r = banco.Set("".join(listaSQL),connector)
                if (r['status'] != 0):
                    print(r)
                total = total + (contador - 1)
                print(total)
                listaSQL = []
                contador = 0    
            i = i + 1    

        if (len(listaSQL) > 0):
            listaSQL.append(') TB ')   
            listaSQL.append(wr)  
            r = banco.Set("".join(listaSQL),connector)
            if (r['status'] != 0):
                print(r)
            total = total + (contador - 1)
            print(total)
            listaSQL = []
            contador = 0
        connector.close()
    except Exception as e:
        retorno = {"status":999,"retorno":str(e)}   

    return retorno

def FormatNull(lista):
    i = 0
    while(i != len(lista)):
        if (lista[i] == 'NULL'):
            lista[i] = None
        i=i+1
    return lista