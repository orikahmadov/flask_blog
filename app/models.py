from datetime import datetime   #Datetime module
from  app import db # login_manager
from flask_login import UserMixin



class User(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String, nullable = False)
    email =  db.Column(db.String(50), nullable = False, unique = True)
    birthday =  db.Column(db.DateTime, nullable =  False)
    password =  db.Column(db.String, nullable =  False)
    nationality =  db.Column(db.String, nullable =  False)
    accept_terms =  db.Column(db.Boolean, nullable =  False, default =  False)
    message =  db.Column(db.Text, nullable =  True)
    account_created =  db.Column(db.DateTime, nullable = False, default  = datetime.now)




    def __repr__(self):
        return f"{self.name}"
    
    
