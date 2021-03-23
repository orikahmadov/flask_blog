from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import json

app =  Flask(__name__)
app.config.from_object("config")
db =  SQLAlchemy(app)
bcrypt =  Bcrypt(app)
# debugger =  DebugToolbarExtension(app)
# login_manager =  LoginManager(app)


countries = []

with open("app/countries.json", "r") as f:
    data =  json.load(f)
    for i in data:
        countries.append(i["country"])






from app import  routes