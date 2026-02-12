from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

aplication = Flask(__name__)
aplication.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
aplication.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

dbase = SQLAlchemy(aplication)
migrate = Migrate(aplication, dbase)

from app.views import home
from app.models import Contacto