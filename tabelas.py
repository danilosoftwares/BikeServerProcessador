class Person:
    def __init__(self,_fields):
        self.BusinessEntityID= _fields[0]
        self.PersonType= _fields[1]
        self.NameStyle= _fields[2]
        self.Title= _fields[3]
        self.FirstName= _fields[4]
        self.MiddleName= _fields[5]
        self.LastName= _fields[6]
        self.Suffix= _fields[7]
        self.EmailPromotion= _fields[8]
        self.AdditionalContactInfo= _fields[9]
        self.Demographics= _fields[10]
        self.rowguid= _fields[11]
        self.ModifiedDate= _fields[12]    

class Customer:
    def __init__(self,_fields):
        self.CustomerID      = _fields[0]
        self.PersonID        = _fields[1]
        self.StoreID         = _fields[2]
        self.TerritoryID     = _fields[3]
        self.AccountNumber   = _fields[4]
        self.rowguid         = _fields[5]
        self.ModifiedDate    = _fields[6]

class SalesOrderHeader:
    def __init__(self,_fields):
        self.SalesOrderID                    = _fields[0]
        self.RevisionNumber                  = _fields[1]
        self.OrderDate                       = _fields[2]
        self.DueDate                         = _fields[3]
        self.ShipDate                        = _fields[4]
        self.Status                          = _fields[5]
        self.OnlineOrderFlag                 = _fields[6]
        self.SalesOrderNumber                = _fields[7]
        self.PurchaseOrderNumber             = _fields[8]
        self.AccountNumber                   = _fields[9]
        self.CustomerID                      = _fields[10]
        self.SalesPersonID                   = _fields[11]
        self.TerritoryID                     = _fields[12]
        self.BillToAddressID                 = _fields[13]
        self.ShipToAddressID                 = _fields[14]
        self.ShipMethodID                    = _fields[15]
        self.CreditCardID                    = _fields[16]
        self.CreditCardApprovalCode          = _fields[17]
        self.CurrencyRateID                  = _fields[18]
        self.SubTotal                        = _fields[19]
        self.TaxAmt                          = _fields[20]
        self.Freight                         = _fields[21]
        self.TotalDue                        = _fields[22]
        self.Comment                         = _fields[23]
        self.rowguid                         = _fields[24]
        self.ModifiedDate                    = _fields[25]

class SalesOrderDetail:
    def __init__(self, _fields):
        self.SalesOrderID             = _fields[0]
        self.SalesOrderDetailID       = _fields[1]
        self.CarrierTrackingNumber    = _fields[2]
        self.OrderQty                 = _fields[3]
        self.ProductID                = _fields[4]
        self.SpecialOfferID           = _fields[5]
        self.UnitPrice                = _fields[6]
        self.UnitPriceDiscount        = _fields[7]
        self.LineTotal                = _fields[8]
        self.rowguid                  = _fields[9]
        self.ModifiedDate             = _fields[10]
    
class SpecialOfferProduct:
    def __init__(self, _fields):
        self.SpecialOfferID = _fields[0]
        self.ProductID= _fields[1]
        self.rowguid= _fields[2]
        self.ModifiedDate= _fields[3]

class Product:
    def __init__(self, _fields):
        self.ProductID                     = _fields[0]
        self.Name                          = _fields[1]
        self.ProductNumber                 = _fields[2]
        self.MakeFlag                      = _fields[3]
        self.FinishedGoodsFlag             = _fields[4]
        self.Color                         = _fields[5]
        self.SafetyStockLevel              = _fields[6]
        self.ReorderPoint                  = _fields[7]
        self.StandardCost                  = _fields[8]
        self.ListPrice                     = _fields[9]
        self.Size                          = _fields[10]
        self.SizeUnitMeasureCode           = _fields[11]
        self.WeightUnitMeasureCode         = _fields[12]
        self.Weight                        = _fields[13]
        self.DaysToManufacture             = _fields[14]
        self.ProductLine                   = _fields[15]
        self.Class                         = _fields[16]
        self.Style                         = _fields[17]
        self.ProductSubcategoryID          = _fields[18]
        self.ProductModelID                = _fields[19]
        self.SellStartDate                 = _fields[20]
        self.SellEndDate                   = _fields[21]
        self.DiscontinuedDate              = _fields[22]
        self.rowguid                       = _fields[23]
        self.ModifiedDate                  = _fields[24]