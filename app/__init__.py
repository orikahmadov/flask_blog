from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app =  Flask(__name__)
app.config.from_object("config")
db =  SQLAlchemy(app)
bcrypt =  Bcrypt(app)
# debugger =  DebugToolbarExtension(app)
login_manager =  LoginManager(app)

