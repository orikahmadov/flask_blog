from app import app, db, bcrypt
from app.forms import RegisterForm
from flask import render_template, redirect, url_for
from app.models import User



@app.route("/")
def index():
    return render_template("index.html")





@app.route("/register", methods=["GET", "POST"])
def register():
    form =  RegisterForm()
    if form.validate_on_submit():
        name =  form.name.data
        email =  form.email.data
        birthday = form.birthday.data
        password  =  form.password.data
        hashed_password =  bcrypt.generate_password_hash(password).decode('utf-8')
        nationality =  form.nationality.data
        accepted =  form.accept_terms.data
        message =  form.message.data
        user =  User(name =  name, email =  email, birthday =  birthday, password  =  hashed_password,
        nationality =  nationality, accept_terms = accepted, message =  message)
        db.session.add(user)
        db.session.commit()
        return "Submitted"
    return render_template("register.html", form =  form)





