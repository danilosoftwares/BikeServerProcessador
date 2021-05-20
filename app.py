
from flask import Flask
import processamento
import upload
import banco

banco.Create()

app = Flask(__name__)

app.add_url_rule('/processar', methods = ['GET'], view_func=processamento.processar)
app.add_url_rule('/arquivos/upload', methods = ['POST'], view_func=upload.upload_file)

@app.route("/")
def hello():
    return "Servico de Processamento Python Ativo!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
