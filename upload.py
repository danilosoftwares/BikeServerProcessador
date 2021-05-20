from flask import jsonify, request

def upload_file():
    if request.method == 'POST':
        for arq in request.files.getlist("file"):
            arq.save(arq.filename)
        return jsonify(status=0,retorno='ok') 