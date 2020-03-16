from flask import Flask, request
from flask_resful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonpify

#connnects database
db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

