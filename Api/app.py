from flask import Flask, jsonify, request
from vendas_dao import *
# Criando uma aplicação Flask com o nome do arquivo atual
app = Flask(__name__)

@app.route('/', methods=['GET'])
def obter_vendas():
    vendas = select_vendas()
    return jsonify(vendas)

@app.route('/<int:id>', methods=['GET'])
def obter_venda_por_id(id):
    venda = select_venda_por_id(id)
    return jsonify(venda)
        
@app.route('/<int:id>', methods=['PUT'])
def editar_venda(id):
    venda = request.get_json()
    nome_produto = venda.get('nome_produto')
    valor = venda.get('valor')
    update_venda(id, nome_produto, valor)
    return obter_vendas()
        

@app.route('/', methods=['POST'])
def incluir_venda():
    nova_venda = request.get_json()
    nome_produto = nova_venda.get('nome_produto')
    valor = nova_venda.get('valor')
    insert_venda(nome_produto, valor)
    return obter_vendas()

@app.route('/<string:nome_produto>', methods=['DELETE'])
def deletar_venda(nome_produto):
    delete_venda(nome_produto)
    return obter_vendas()




app.run(port=5000,host='localhost',debug=True)