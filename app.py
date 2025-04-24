from flask import Flask, request, jsonify
from models import db, Cliente, Veiculo, OrdemServico

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulador.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    telefone = data.get('telefone')

    if not nome or not email or not telefone:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    cliente = Cliente(nome=nome, email=email, telefone=telefone)
    db.session.add(cliente)
    db.session.commit()

    return jsonify({"message": "Cliente cadastrado com sucesso!"}), 201

@app.route('/veiculos/<int:cliente_id>', methods=['POST'])
def cadastrar_veiculo(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    data = request.get_json()
    modelo = data.get('modelo')
    placa = data.get('placa')

    if not modelo or not placa:
        return jsonify({"error": "Modelo e placa são obrigatórios!"}), 400

    veiculo = Veiculo(modelo=modelo, placa=placa, cliente_id=cliente.id)
    db.session.add(veiculo)
    db.session.commit()

    return jsonify({"message": "Veículo cadastrado com sucesso!"}), 201

@app.route('/ordens_servico/<int:veiculo_id>', methods=['POST'])
def registrar_ordem_servico(veiculo_id):
    veiculo = Veiculo.query.get_or_404(veiculo_id)
    data = request.get_json()
    descricao = data.get('descricao')
    status = data.get('status')

    if not descricao or not status:
        return jsonify({"error": "Descrição e status são obrigatórios!"}), 400

    ordem_servico = OrdemServico(descricao=descricao, status=status, veiculo_id=veiculo.id)
    db.session.add(ordem_servico)
    db.session.commit()

    return jsonify({"message": "Ordem de serviço registrada com sucesso!"}), 201

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{'id': c.id, 'nome': c.nome, 'email': c.email, 'telefone': c.telefone} for c in clientes])

@app.route('/veiculos/<int:cliente_id>', methods=['GET'])
def listar_veiculos(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    veiculos = Veiculo.query.filter_by(cliente_id=cliente.id).all()
    return jsonify([{'id': v.id, 'modelo': v.modelo, 'placa': v.placa} for v in veiculos])

@app.route('/ordens_servico', methods=['GET'])
def listar_ordens_servico():
    status = request.args.get('status')
    veiculo_id = request.args.get('veiculo_id', type=int)

    query = OrdemServico.query

    if status:
        query = query.filter_by(status=status)
    if veiculo_id:
        query = query.filter_by(veiculo_id=veiculo_id)

    ordens = query.all()
    return jsonify([{'id': o.id, 'descricao': o.descricao, 'status': o.status} for o in ordens])

@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    data = request.get_json()
    cliente = Cliente.query.get_or_404(id)

    cliente.nome = data.get('nome', cliente.nome)
    cliente.email = data.get('email', cliente.email)
    cliente.telefone = data.get('telefone', cliente.telefone)

    db.session.commit()

    return jsonify({"message": "Cliente atualizado com sucesso!"})

@app.route('/veiculos/<int:id>', methods=['PUT'])
def atualizar_veiculo(id):
    data = request.get_json()
    veiculo = Veiculo.query.get_or_404(id)

    veiculo.modelo = data.get('modelo', veiculo.modelo)
    veiculo.placa = data.get('placa', veiculo.placa)

    db.session.commit()

    return jsonify({"message": "Veículo atualizado com sucesso!"})

@app.route('/ordens_servico/<int:id>', methods=['PUT'])
def atualizar_ordem_servico(id):
    data = request.get_json()
    ordem = OrdemServico.query.get_or_404(id)

    ordem.descricao = data.get('descricao', ordem.descricao)
    ordem.status = data.get('status', ordem.status)

    db.session.commit()

    return jsonify({"message": "Ordem de serviço atualizada com sucesso!"})

@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente excluído com sucesso!"})

@app.route('/veiculos/<int:id>', methods=['DELETE'])
def excluir_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    return jsonify({"message": "Veículo excluído com sucesso!"})

@app.route('/ordens_servico/<int:id>', methods=['DELETE'])
def excluir_ordem_servico(id):
    ordem = OrdemServico.query.get_or_404(id)
    db.session.delete(ordem)
    db.session.commit()
    return jsonify({"message": "ordem de serviço atualizada com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)