from operator import truediv

from flask.wrappers import Request
from config import *
from modelo import *

@app.route("/")
def inicio():
    return 'Sistema de Cadastro Personagens' +\
        '<a href= "/listar_turmadamonica">Operação listar</a>'

#Função Lista Genérica
@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Pessoa": #1
        dados = db.session.query(Pessoa).all()
    elif classe == "Relacao": #2 
        dados = db.session.query(Relacao).all()
    elif classe == "Caracteristicas": #3
        dados = db.session.query(Caracteristicas).all()    
    elif classe == "Brincadeira": #4
        dados = db.session.query(Brincadeira).all()
    elif classe == "Especialidade": #5
        dados = db.session.query(Especialidade).all()    
    elif classe == "Pet": #6
        dados = db.session.query(Pet).all()
    elif classe == "Pai": #7
        dados = db.session.query(Pai).all()
    elif classe == "Mae": #8
        dados = db.session.query(Mae).all()
    elif classe == "Vestimenta": #9
        dados = db.session.query(Vestimenta).all()
    elif classe == "Personagem": #10
        dados = db.session.query(Personagem).all()
    #Converter dados para json
    lista_jsons = [x.json() for x in dados]
    #Converter a lista de Python para json
    resposta = jsonify(lista_jsons)
    #Permitir resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

#Iincluir 

#1 Classe Pessoa
@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Pessoa(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#2 Classe Relacao
@app.route("/incluir_relacao", methods=['post'])
def incluir_relacao():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Relacao(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#3 Classe Caracteristicas
@app.route("/incluir_caracteristicas", methods=['post'])
def incluir_caracteristicas():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Caracteristicas(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#4 Classe Brincadeira
@app.route("/incluir_brincadeira", methods=['post'])
def incluir_brincadeira():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Brincadeira(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#5 Classe Especialidade
@app.route("/incluir_especialidade", methods=['post'])
def incluir_especialidade():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Especialidade(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#6 Classe Pet
@app.route("/incluir_pet", methods=['post'])
def incluir_pet():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Pet(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#7 Classe Pai
@app.route("/incluir_pai", methods=['post'])
def incluir_pai():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Pai(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#8 Classe Mae
@app.route("/incluir_mae", methods=['post'])
def incluir_mae():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Mae(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#9 Classe Vestimenta
@app.route("/incluir_vestimenta", methods=['post'])
def incluir_vestimenta():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Vestimenta(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#10 Classe Personagem
@app.route("/incluir_personagem", methods=['post'])
def incluir_personagem():
    resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
    dados = Request.get_json()
    try:
        novo = Personagem(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado" : "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

app.run(debug=True)
