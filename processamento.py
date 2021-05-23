import banco

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


def ApagaTudo():
    retorno = {"status":0,"retorno":"ok"}   
    try:    
        connector = banco.GetConnector()
        tabs = ['customer','person','product','salesorderdetail','salesorderheader','specialofferproduct']
        for t in tabs:
            r = banco.Set("DELETE from "+t,connector)
            if (r['status'] != 0):
                print(r)
                retorno = r
                break
        connector.close()
    except Exception as e:
        retorno = {"status":999,"retorno":str(e)}                   
    return retorno      