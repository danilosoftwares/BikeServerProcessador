from flask import Flask, render_template
import upload
import relatorio
import processamento
import banco

banco.Create()

app = Flask(__name__)

app.add_url_rule('/relatorio/person', methods = ['GET'], view_func=relatorio.relatorioPerson)
app.add_url_rule('/relatorio/customer', methods = ['GET'], view_func=relatorio.relatorioCustomer)
app.add_url_rule('/relatorio/specialofferproduct', methods = ['GET'], view_func=relatorio.relatorioSpecialOfferProduct)
app.add_url_rule('/relatorio/product', methods = ['GET'], view_func=relatorio.relatorioProduct)
app.add_url_rule('/relatorio/salesorderheader', methods = ['GET'], view_func=relatorio.relatorioSalesOrderHeader)
app.add_url_rule('/relatorio/salesorderdetail', methods = ['GET'], view_func=relatorio.relatorioSalesOrderDetail)
app.add_url_rule('/arquivos/upload', methods = ['POST'], view_func=upload.upload_file)
app.add_url_rule('/banco/apagar', methods = ['POST'], view_func=processamento.ApagaTudo)

@app.route("/")
def hello():
    return render_template('index.html')
    #return "Servico de Processamento Python Ativo!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
