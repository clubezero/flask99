from app import aplication
from flask import render_template, url_for

@aplication.route('/')

def home():
	return render_template('index.html')

@aplication.route('/elencos')
def page():
	return "Nova pagina"