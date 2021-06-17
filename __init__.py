from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://saydxuhiccphbg:b5709ece099cb5be7e15bd75ec378352e4d762519bbcc57983ddcf6a34c9286d@ec2-52-213-167-210.eu-west-1.compute.amazonaws.com:5432/daen84vkh5qmil'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.init_app(app)