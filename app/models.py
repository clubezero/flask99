from app import dbase
from datetime import datetime

class Contacto(dbase.Model):
    id = dbase.Column(dbase.Integer, primary_key=True)
    data_envio = dbase.Column(dbase.DateTime, default=datetime.utcnow) # Recomendado usar utcnow
    nome = dbase.Column(dbase.String(100), nullable=True) # É boa prática definir um tamanho para String
    email = dbase.Column(dbase.String(120), nullable=True)
    assunto = dbase.Column(dbase.String(200), nullable=True)
    messagem = dbase.Column(dbase.Text, nullable=True) # 'Text' é melhor para mensagens longas
    respodido = dbase.Column(dbase.Integer, default = 0)