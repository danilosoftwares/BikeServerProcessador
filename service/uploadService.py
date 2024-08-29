from flask import jsonify, request

import service.integrationService as integrationService
import models.tablesModel as tablesModel

def upload_file():
    try:
        retorno = {"status":997,"retorno":'nenhum arquivo encontrado no payload'}   
        if request.method == 'POST':
            for arq in request.files.getlist("file"):
                lista = arq.read()
                lista = lista.decode('utf-8')
                lista = lista.split('\n')
                if (arq.filename.upper() == 'PERSON.PERSON.CSV'):
                    retorno = integrationService.Gravador(lista,tablesModel.Person, 1000)
                elif (arq.filename.upper() == 'SALES.CUSTOMER.CSV'):
                    retorno =(integrationService.Gravador(lista,tablesModel.Customer, 1000)) 
                elif (arq.filename.upper() == 'SALES.SALESORDERHEADER.CSV'):
                    retorno =(integrationService.Gravador(lista,tablesModel.SalesOrderHeader, 300)) 
                elif (arq.filename.upper() == 'SALES.SALESORDERDETAIL.CSV'):
                    retorno =(integrationService.Gravador(lista,tablesModel.SalesOrderDetail, 300)) 
                elif (arq.filename.upper() == 'SALES.SPECIALOFFERPRODUCT.CSV'):
                    retorno =(integrationService.Gravador(lista,tablesModel.SpecialOfferProduct, 1000)) 
                elif (arq.filename.upper() == 'PRODUCTION.PRODUCT.CSV'):
                    retorno =(integrationService.Gravador(lista,tablesModel.Product, 1000)) 
                else:
                    retorno = {"status":998,"retorno":'arquivo nao faz parte da lista de arquivos tratados pela api'}      

    except Exception as e:
        retorno = {"status":999,"retorno":str(e)}   
    return jsonify(retorno)