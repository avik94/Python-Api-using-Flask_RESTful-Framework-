
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# from model import *

db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/avik/Documents/api/product.db'
    initialize_extensions(app)
    db.init_app(app)
    return app

def initialize_extensions(app):
    from app.resource.employeeDetails import Employee
    from app.resource.employeeSportsDetails import Sports

    api = Api(app)
    api.add_resource(Employee, "/employee")
    api.add_resource(Sports, "/sports")
