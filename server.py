from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify


db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() #connect to database
        query = conn.execute("select * from employees") #SQL Query and returns Json
        return {'employees': [i[0] for i in query.cursor.fetchall() ]} # Fetches the fist column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()) , i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.conect()
        query = conn.execute("select * from employees where Employee_ID =%d" %int(employee_id))
        result = {'data':[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)