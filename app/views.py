from app import aplication, dbase
from flask import render_template, url_for, request

from app.models import Contacto

@aplication.route('/')

def home():
	return render_template('index.html')

@aplication.route('/contacto', methods=['GET','POST'])
def page():
	context ={}
	if request.method == 'GET':
		pesquisa = request.args.get('pesquisa')
		context.update({'pesquisa': pesquisa})
	if request.method == 'POST':
		nome = request.form['nome']
		email = request.form['email']
		assunto = request.form['assunto']
		messagem = request.form['messagem']

		contacto = Contacto(
			nome = nome,
			email = email,
			assunto = assunto,
			messagem = messagem
		)

		dbase.session.add(contacto)
		dbase.session.commit()


	return render_template('contacto.html', context=context)