from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b794ae7cfb67312a519fa2e2'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes