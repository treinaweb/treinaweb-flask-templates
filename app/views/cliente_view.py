from flask import render_template, redirect, url_for, request

from app.forms import cliente_form

from app import app
from app.models import cliente_model
from app.entidades import cliente
from app.services import cliente_service

@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data

        cliente = cliente_model.Cliente(nome=nome, email=email, data_nascimento=data_nascimento, profissao=profissao)
        try:
            cliente_service.cadastrar_cliente(cliente)
            return redirect(url_for("listar_clientes"))
        except:
            print("Cliente não cadastrado")

    return render_template("clientes/cadastrar_cliente.html")

@app.route("/listar_clientes", methods=["GET"])
def listar_clientes():
    clientes = cliente_service.listar_clientes()
    return render_template("clientes/lista_clientes.html")