from flask import Flask, request
from flask_resful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonpify


db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() #connect to database
        query = conn.execute("select * from employees") #SQL Query and returns Json
        