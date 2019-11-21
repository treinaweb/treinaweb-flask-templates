from app import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    data_nascimento = db.Column(db.DateTime)
    profissao = db.Column(db.String(30))
