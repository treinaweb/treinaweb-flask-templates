from app.models import cliente_model
from app import db

def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return clientes

def cadastrar_cliente(cliente):
    db.session.add(cliente)
    db.session.commit()