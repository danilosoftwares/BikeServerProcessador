from flask import Flask, render_template
import service.uploadService as uploadService
import service.reportService as reportService
import service.integrationService as integrationService
import database.database as database

database.Create()

app = Flask(__name__)

app.add_url_rule('/report/person', methods = ['GET'], view_func=reportService.reportPerson)
app.add_url_rule('/report/customer', methods = ['GET'], view_func=reportService.reportCustomer)
app.add_url_rule('/report/specialofferproduct', methods = ['GET'], view_func=reportService.reportSpecialOfferProduct)
app.add_url_rule('/report/product', methods = ['GET'], view_func=reportService.reportProduct)
app.add_url_rule('/report/salesorderheader', methods = ['GET'], view_func=reportService.reportSalesOrderHeader)
app.add_url_rule('/report/salesorderdetail', methods = ['GET'], view_func=reportService.reportSalesOrderDetail)
app.add_url_rule('/files/upload', methods = ['POST'], view_func=uploadService.upload_file)
app.add_url_rule('/registers/clean', methods = ['POST'], view_func=integrationService.CleanAll)

@app.route("/")
def indexPage():
    return render_template('index.html')
    #return "Servico de Processamento Python Ativo!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
