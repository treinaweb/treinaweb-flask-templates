from flask import render_template, redirect, url_for, request, session

from app.forms import cliente_form

from app import app, babel
from app.models import cliente_model
from app.entidades import cliente
from app.services import cliente_service

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'pt')

@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    clientes = cliente_service.listar_clientes()
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

    return render_template('clientes/cadastrar_cliente.html', form_template=form, clientes_template=clientes)

@app.route("/listar_clientes", methods=["GET"])
def listar_clientes():
    clientes = cliente_service.listar_clientes()
    return render_template('clientes/lista_clientes.html', clientes_template=clientes)