import tabelas

def processar():        
    ps = Listar('person.person.csv',tabelas.Person)    
    ct  = Listar('Sales.Customer.csv',tabelas.Customer)
    soh  = Listar('Sales.SalesOrderHeader.csv',tabelas.SalesOrderHeader)
    sod  = Listar('Sales.SalesOrderDetail.csv',tabelas.SalesOrderDetail)
    sop  = Listar('Sales.SpecialOfferProduct.csv',tabelas.SpecialOfferProduct)
    pd  = Listar('Production.Product.csv',tabelas.Product)    
    return 'p.lista'

def Listar(file, classe):
    f = open(file, "r")
    lista = f.read().split('\n')
    lista = lista[1:len(lista)]
    i = 0
    while(i < len(lista)):
        if (lista[i] != ''):
            lista[i] = classe(lista[i].split(';'))
        i=i+1
    return lista