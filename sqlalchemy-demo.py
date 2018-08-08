from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET'] = 'ABCD'
app.config['SQLALCHEMY_DATABASE_URL'] = \
        'mysql://root:123456@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, nullable=False, primary_key=True,
            autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='',
            unique=True)
