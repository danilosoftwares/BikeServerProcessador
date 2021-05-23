from flask import jsonify, request

import processamento
import tabelas

def upload_file():
    try:
        retorno = {"status":997,"retorno":'nenhum arquivo encontrado no payload'}   
        if request.method == 'POST':
            for arq in request.files.getlist("file"):
                lista = arq.read()
                lista = lista.decode('utf-8')
                lista = lista.split('\r')
                if (arq.filename.upper() == 'PERSON.PERSON.CSV'):
                    retorno = processamento.Gravador(lista,tabelas.Person, 1000)
                elif (arq.filename.upper() == 'SALES.CUSTOMER.CSV'):
                    retorno =(processamento.Gravador(lista,tabelas.Customer, 1000)) 
                elif (arq.filename.upper() == 'SALES.SALESORDERHEADER.CSV'):
                    retorno =(processamento.Gravador(lista,tabelas.SalesOrderHeader, 300)) 
                elif (arq.filename.upper() == 'SALES.SALESORDERDETAIL.CSV'):
                    retorno =(processamento.Gravador(lista,tabelas.SalesOrderDetail, 300)) 
                elif (arq.filename.upper() == 'SALES.SPECIALOFFERPRODUCT.CSV'):
                    retorno =(processamento.Gravador(lista,tabelas.SpecialOfferProduct, 1000)) 
                elif (arq.filename.upper() == 'PRODUCTION.PRODUCT.CSV'):
                    retorno =(processamento.Gravador(lista,tabelas.Product, 1000)) 
                else:
                    retorno = {"status":998,"retorno":'arquivo nao faz parte da lista de arquivos tratados pela api'}      

    except Exception as e:
        retorno = {"status":999,"retorno":str(e)}   
    return jsonify(retorno)