from app import aplication
from flask import render_template

@aplication.route('/')

def home():
	return render_template('index.html')