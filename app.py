
from flask import Flask
import processamento
import upload
import banco

banco.Create()

app = Flask(__name__)

app.add_url_rule('/processar/person', methods = ['GET'], view_func=processamento.processar_person)
app.add_url_rule('/processar/customer', methods = ['GET'], view_func=processamento.processar_customer)
app.add_url_rule('/processar/header', methods = ['GET'], view_func=processamento.processar_SalesOrderHeader)
app.add_url_rule('/processar/detail', methods = ['GET'], view_func=processamento.processar_SalesOrderDetail)
app.add_url_rule('/processar/special', methods = ['GET'], view_func=processamento.processar_SpecialOfferProduct)
app.add_url_rule('/processar/product', methods = ['GET'], view_func=processamento.processar_product)
app.add_url_rule('/processar/all', methods = ['GET'], view_func=processamento.processar_all)


app.add_url_rule('/arquivos/upload', methods = ['POST'], view_func=upload.upload_file)

@app.route("/")
def hello():
    return "Servico de Processamento Python Ativo!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
