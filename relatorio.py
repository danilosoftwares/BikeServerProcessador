import banco
from flask import render_template_string

def relatorioPerson():
    return relatorio_generic('Person',['BusinessEntityID','FirstName','MiddleName','LastName'])

def relatorioCustomer():
    return relatorio_generic('Customer',['CustomerID' ,'PersonID' ,'StoreID' ,'TerritoryID' ,'AccountNumber'])
  
def relatorioSpecialOfferProduct():
    return relatorio_generic('SpecialOfferProduct',['SpecialOfferID','ProductID','rowguid'])

def relatorioSalesOrderHeader():
    return relatorio_generic('SalesOrderHeader',['SalesOrderID','RevisionNumber','OrderDate','DueDate','ShipDate','Status'])

def relatorioSalesOrderDetail():
    return relatorio_generic('SalesOrderDetail',['SalesOrderID','SalesOrderDetailID' ,'CarrierTrackingNumber','OrderQty','ProductID'])

def relatorioProduct():
    return relatorio_generic('Product',['ProductID','Name','ProductNumber','MakeFlag','FinishedGoodsFlag','Color','SafetyStockLevel','ReorderPoint','StandardCost','ListPrice','Size'])


def relatorio_generic(_tab, _campos):
    lista = banco.Get('SELECT '+','.join(_campos)+' FROM '+_tab+' ORDER BY '+_campos[0]+' limit 500')
    return render_template_string(layout_relatorio(_tab,lista,_campos))


def layout_relatorio(_nome,_lista, _colunas):
    layout = """
            <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        }

        td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
        }

        tr:nth-child(even) {
        background-color: #dddddd;
        }
        </style>
        </head>
        <body>

        <h2>

        """

    layout += _nome
    layout += '</h2><table>'

    layout += '<tr>'
    y = 0
    while(y != len(_colunas)):
        layout += '<th>'+str(_colunas[y])+'</th>'
        y=y+1
    layout += '</tr>'
 

    i = 0
    while(i != len(_lista)):
        layout += '<tr>'
        y = 0
        while(y != len(_lista[0])):
            layout += '<td>'+str(_lista[i][y])+'</td>'
            y=y+1
        layout += '</tr>'
        i=i+1

    layout += """</table></body></html>"""    
    return layout