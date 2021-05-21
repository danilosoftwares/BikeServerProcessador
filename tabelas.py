from datetime import datetime

def FromValue(_value):
    t = str(type(_value).__name__)
    if (t == 'int'):
        retorno = str(_value)
    elif (t == 'float'):
        retorno = str(_value)
    elif (t == 'datetime'):
        retorno = '"'+str(_value)+'"'
    elif (t == 'NoneType'):
        retorno = str('null')
    elif (str(_value).find('"') > -1):
        retorno = """"""+str(_value)+""""""
    else:
        retorno = '"'+str(_value)+'"'
    return retorno

def ToInteger(_value):
    retorno = _value 
    if (_value == None): 
        retorno = None 
    else:
        retorno = int(retorno)
    return retorno

def ToDateTime(_value):
    retorno = _value 
    if (_value == None): 
        retorno = None 
    else:
        retorno = datetime.fromisoformat(retorno)
    return retorno 

def ToFloat(_value):
    retorno = _value 
    if (_value == None): 
        retorno = None 
    else:
        retorno = float(retorno.replace(',','.'))
    return retorno 

def ToString(_value):
    retorno = _value 
    if (_value == None): 
        retorno = None 
    return retorno 

def GetAttr(cls):   
    return [i for i in cls.__dict__.keys() if i[:1] != '_']         

def GetLineSQL(cls):
    colunas = ''
    valores = ''
    campos = GetAttr(cls)
    i = 0
    while(i < len(campos)):
        if (i > 0):
            colunas = colunas + ','
            valores = valores + ','

        colunas = colunas + campos[i]
        valores = valores + FromValue(getattr(cls, campos[i]))+' as '+campos[i]

        i = i + 1   

    return [colunas,valores]

class BaseAll:
    keys = []

    def ProcessSQL(self):
        tmp = GetLineSQL(self)
        self.Colunas = tmp[0]
        self.Valores = tmp[1]           

    def WhereSQL(self):
        retorno = 'WHERE NOT EXISTS (select '+self.keys[0]+' from '+type(self).__name__+' where '
        i = 0
        while( i != len(self.keys)):
            if (i > 0):
                retorno = retorno + ' AND '
            retorno = retorno +' '+ self.keys[i] + ' = TB.'+self.keys[i]
            i=i+1
        retorno = retorno + ' )'
        return retorno

class Person(BaseAll):
    def __init__(self,_fields):
        self.BusinessEntityID= ToInteger(_fields[0])
        self.PersonType= ToString(_fields[1])
        self.NameStyle= ToInteger(_fields[2])
        self.Title= ToString(_fields[3])
        self.FirstName= ToString(_fields[4])
        self.MiddleName= ToString(_fields[5])
        self.LastName=ToString( _fields[6])
        self.Suffix= ToString(_fields[7])
        self.EmailPromotion= ToInteger(_fields[8])
        self.AdditionalContactInfo=ToString( _fields[9])
        self.Demographics= ToString(_fields[10])
        self.rowguid= ToString(_fields[11])
        self.ModifiedDate= ToDateTime( _fields[12])  
        self.ProcessSQL()
        self.keys = ['BusinessEntityID']

class Customer(BaseAll):
    def __init__(self,_fields):
        self.CustomerID      = ToInteger(_fields[0])
        self.PersonID        = ToInteger(_fields[1])
        self.StoreID         = ToInteger(_fields[2])
        self.TerritoryID     = ToInteger(_fields[3])
        self.AccountNumber   = ToString(_fields[4])
        self.rowguid         = ToString(_fields[5])
        self.ModifiedDate    = ToDateTime( _fields[6])  
        self.ProcessSQL()
        self.keys = ['CustomerID']

class SalesOrderHeader(BaseAll):
    def __init__(self,_fields):
        self.SalesOrderID                    = ToInteger(_fields[0])
        self.RevisionNumber                  = ToInteger(_fields[1])
        self.OrderDate                       = ToDateTime(_fields[2])
        self.DueDate                         = ToDateTime(_fields[3])
        self.ShipDate                        = ToDateTime(_fields[4])
        self.Status                          = ToInteger(_fields[5])
        self.OnlineOrderFlag                 = ToInteger(_fields[6])
        self.SalesOrderNumber                = ToString(_fields[7])
        self.PurchaseOrderNumber             = ToString(_fields[8])
        self.AccountNumber                   = ToString(_fields[9])
        self.CustomerID                      = ToInteger(_fields[10])
        self.SalesPersonID                   = ToInteger(_fields[11])
        self.TerritoryID                     = ToInteger(_fields[12])
        self.BillToAddressID                 = ToInteger(_fields[13])
        self.ShipToAddressID                 = ToInteger(_fields[14])
        self.ShipMethodID                    = ToInteger(_fields[15])
        self.CreditCardID                    = ToInteger(_fields[16])
        self.CreditCardApprovalCode          = ToString(_fields[17])
        self.CurrencyRateID                  = ToInteger(_fields[18])
        self.SubTotal                        = ToFloat(_fields[19])
        self.TaxAmt                          = ToFloat(_fields[20])
        self.Freight                         = ToFloat(_fields[21])
        self.TotalDue                        = ToFloat(_fields[22])
        self.Comment                         = ToString(_fields[23])
        self.rowguid                         = ToString(_fields[24])
        self.ModifiedDate                    = ToDateTime(_fields[25])
        self.ProcessSQL()
        self.keys = ['SalesOrderID']

class SalesOrderDetail(BaseAll):
    def __init__(self, _fields):
        self.SalesOrderID             = ToInteger(_fields[0])
        self.SalesOrderDetailID       = ToInteger(_fields[1])
        self.CarrierTrackingNumber    = ToString(_fields[2])
        self.OrderQty                 = ToInteger(_fields[3])
        self.ProductID                = ToInteger(_fields[4])
        self.SpecialOfferID           = ToInteger(_fields[5])
        self.UnitPrice                = ToFloat(_fields[6])
        self.UnitPriceDiscount        = ToFloat(_fields[7])
        self.LineTotal                = ToFloat(_fields[8])
        self.rowguid                  = ToString(_fields[9])
        self.ModifiedDate             = ToDateTime(_fields[10])
        self.ProcessSQL()
        self.keys = ['SalesOrderID','SalesOrderDetailID']
    
class SpecialOfferProduct(BaseAll):
    def __init__(self, _fields):
        self.SpecialOfferID = ToInteger(_fields[0])
        self.ProductID= ToInteger(_fields[1])
        self.rowguid   = ToString(_fields[2])
        self.ModifiedDate   = ToDateTime(_fields[3])
        self.ProcessSQL()
        self.keys = ['ProductID','SpecialOfferID']

class Product(BaseAll):
    def __init__(self, _fields):
        self.ProductID                     =  ToInteger(_fields[0])
        self.Name                          = ToString(_fields[1])
        self.ProductNumber                 = ToString(_fields[2])
        self.MakeFlag                      = ToInteger(_fields[3])
        self.FinishedGoodsFlag             = ToInteger(_fields[4])
        self.Color                         = ToString(_fields[5])
        self.SafetyStockLevel              = ToInteger(_fields[6])
        self.ReorderPoint                  = ToInteger(_fields[7])
        self.StandardCost                  = ToFloat(_fields[8])
        self.ListPrice                     = ToFloat(_fields[9])
        self.Size                          = ToString(_fields[10])
        self.SizeUnitMeasureCode           = ToString(_fields[11])
        self.WeightUnitMeasureCode         = ToString(_fields[12])
        self.Weight                        = ToFloat(_fields[13])
        self.DaysToManufacture             = ToInteger(_fields[14])
        self.ProductLine                   = ToString(_fields[15])
        self.Class                         = ToString(_fields[16])
        self.Style                         = ToString(_fields[17])
        self.ProductSubcategoryID          = ToInteger(_fields[18])
        self.ProductModelID                = ToInteger(_fields[19])
        self.SellStartDate                 = ToDateTime(_fields[20])
        self.SellEndDate                   = ToDateTime(_fields[21])
        self.DiscontinuedDate              = ToDateTime(_fields[22])
        self.rowguid   = ToString(_fields[23])
        self.ModifiedDate   = ToDateTime(_fields[24])
        self.ProcessSQL()
        self.keys = ['ProductID']