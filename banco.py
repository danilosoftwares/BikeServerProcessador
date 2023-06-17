import mysql.connector

v_user="root"
v_password='root'
v_host="mydb"
v_port=3306
v_database='bike'


def GetConnector():
        return mysql.connector.connect(user=v_user, password=v_password, host=v_host, port=v_port, database=v_database)

def Create():


        conn = mysql.connector.connect(user=v_user, password=v_password, host=v_host, port=v_port)  
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS "+v_database)

        person = """
        CREATE TABLE IF NOT EXISTS  Person
        (
                BusinessEntityID int(11) not null primary key,
                PersonType varchar(10),
                NameStyle  int(11) ,
                Title varchar(10),
                FirstName varchar(100),
                MiddleName varchar(100),
                LastName varchar(100),
                Suffix varchar(10),
                EmailPromotion int(11),
                AdditionalContactInfo text,
                Demographics text,
                rowguid varchar(100),
                ModifiedDate timestamp
        )
        """
        customer = """
        CREATE TABLE IF NOT EXISTS  Customer
        (
                CustomerID int(11) not null primary key,
                PersonID int(11),
                StoreID int(11),
                TerritoryID int(11),
                AccountNumber varchar(30),								
                rowguid varchar(100),
                ModifiedDate timestamp
        )					
        """

        SalesOrderDetail = """
        CREATE TABLE IF NOT EXISTS  SalesOrderDetail
        (
                SalesOrderID int(11) not null ,
                SalesOrderDetailID int(11) not null,
                CarrierTrackingNumber varchar(30),								
                OrderQty int(11),								
                ProductID int(11),		
                SpecialOfferID int(11),
                UnitPrice float,
                UnitPriceDiscount float,
                LineTotal float,			
                rowguid varchar(100),
                ModifiedDate timestamp,
                PRIMARY KEY (SalesOrderID,SalesOrderDetailID)
        )
        """

        especial = """
        CREATE TABLE IF NOT EXISTS  SpecialOfferProduct
        (				
                SpecialOfferID int(11)  not null,
                ProductID int(11) not null,		
                rowguid varchar(100),
                ModifiedDate timestamp,
                PRIMARY KEY (ProductID,SpecialOfferID)
        )
        """

        header = """
        CREATE TABLE IF NOT EXISTS  SalesOrderHeader
        (				
                SalesOrderID int(11)  not null,
                RevisionNumber int(11),	
                OrderDate timestamp,
                DueDate timestamp default CURRENT_TIMESTAMP NOT NULL,
                ShipDate timestamp default CURRENT_TIMESTAMP NOT NULL,
                Status int(11),
                OnlineOrderFlag int(11),
                SalesOrderNumber VARCHAR(30),
                PurchaseOrderNumber varchar(30),
                AccountNumber varchar(30),
                CustomerID int(11),
                SalesPersonID int(11),
                TerritoryID int(11),
                BillToAddressID int(11),
                ShipToAddressID int(11),
                ShipMethodID int(11),
                CreditCardID int(11),
                CreditCardApprovalCode varchar(30),
                CurrencyRateID int(11),
                SubTotal float,
                TaxAmt float,
                Freight float,
                TotalDue float,
                Comment text,
                rowguid varchar(100),
                ModifiedDate timestamp default CURRENT_TIMESTAMP NOT NULL,
                PRIMARY KEY (SalesOrderID)
        )

        """

        product = """
        CREATE TABLE IF NOT EXISTS  Product
        (				
                ProductID int(11)  not null,
                Name varchar(500),
                ProductNumber varchar(30),	
                MakeFlag int(11),
                FinishedGoodsFlag int(11),
                Color varchar(30),
                SafetyStockLevel int(11),
                ReorderPoint int(11),
                StandardCost float,
                ListPrice float,
                Size varchar(10),
                SizeUnitMeasureCode varchar(10),
                WeightUnitMeasureCode varchar(10),
                Weight float,
                DaysToManufacture int(11),
                ProductLine varchar(10),
                Class varchar(10),
                Style varchar(10),
                ProductSubcategoryID int(11),
                ProductModelID int(11),
                SellStartDate timestamp default CURRENT_TIMESTAMP NOT NULL,
                SellEndDate timestamp default CURRENT_TIMESTAMP NOT NULL,
                DiscontinuedDate timestamp default CURRENT_TIMESTAMP NOT NULL,
                rowguid varchar(100),
                ModifiedDate timestamp default CURRENT_TIMESTAMP NOT NULL,
                PRIMARY KEY (ProductID)
        )

        """

        conn = mysql.connector.connect(user=v_user, password=v_password, host=v_host, port=v_port, database=v_database)        
        Set(person, conn)
        Set(customer,conn)
        Set(SalesOrderDetail,conn)
        Set(especial,conn)
        Set(header,conn)
        Set(product,conn)
        conn.close()

def Set(comando, _conn=None):
        retorno = {"status":0}
        if (_conn != None):
                conn = _conn
        else:
                conn = mysql.connector.connect(user=v_user, password=v_password, host=v_host, port=v_port, database=v_database)                
        try:
                cursor = conn.cursor()
                cursor.execute(comando)
                conn.commit()
        except Exception as e:                
                conn.rollback()
                retorno = {"status":999,"error":str(e)}
        if (_conn == None):
                conn.close()
        return retorno

def Get(comando, _conn=None):
        if (_conn != None):
                conn = _conn
        else:
                conn = mysql.connector.connect(user=v_user, password=v_password, host=v_host, port=v_port, database=v_database)                
        cursor = conn.cursor()
        cursor.execute(comando)
        retorno = []
        for linha in cursor.fetchall():
                retorno.append(linha)         
        if (_conn == None):
                conn.close()
        return retorno

def SetBlock(_lista, _conn=None):
        retorno = {"status":0}
        if (_conn != None):
                conn = _conn
        else:
                conn = mysql.connector.connect(user=v_user, password=v_password, host=v_host, port=v_port, database=v_database)                

        comando = ""


        try:
                cursor = conn.cursor()
                cursor.execute(comando)
                conn.commit()
        except Exception as e:                
                conn.rollback()
                retorno = {"status":999,"error":str(e)}
        if (_conn == None):
                conn.close()
        return retorno