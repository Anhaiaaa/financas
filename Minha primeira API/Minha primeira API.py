from flask import Flask, jsonify

app= Flask(__name__)

@app.route('/')
def home_page():
    return'Bem vindo'

@app.route('/nomes')
def pegar_nome():
    nomes=['lucas anhaia','Jeremias','Leticia']

    return jsonify(nomes)
    
app.run()
    