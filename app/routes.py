from flask import render_template, redirect, url_for, flash
from app import app, db, bcrypt
from app.forms import RegisterForm
from app.models import User
from werkzeug.utils import secure_filename
import secrets, os
from datetime import datetime

@app.route("/")
def index():
    return render_template("index.html")



def save_photo(file):
    file_extension =  os.path.splitext(file)[-1]
    changed_name =  secrets.token_hex(8)
    file_full_name =  changed_name + file_extension
    return file_full_name





@app.route("/register", methods=["GET", "POST"])
def register():
    form =  RegisterForm()
    if form.validate_on_submit():
        if  form.photo.data:     #If user wants to upload a photo
            photo =  form.photo.data
            filename  =  secure_filename(photo.filename)
            changed_name =  save_photo(filename)
            photo.save(os.path.join(app.config["UPLOAD_PATH"], changed_name))
            user =  User(name =  form.name.data, email =  form.email.data,
            birthday =  form.birthday.data, password  =  bcrypt.generate_password_hash(form.password.data).decode("utf-8"),
            nationality =  form.nationality.data, accept_terms = form.accept_terms.data, gender =  form.gender.data,
            message =  form.message.data, photo =  changed_name)
            db.session.add(user)
            db.session.commit()
            print("Submitted")
            return redirect(url_for("index"))
        else:
            user = User(name=form.name.data, email=form.email.data,
                        birthday=form.birthday.data,
                        password=bcrypt.generate_password_hash(form.password.data).decode("utf-8"),
                        nationality=form.nationality.data, accept_terms=form.accept_terms.data, gender =  form.gender.data,
                        message=form.message.data, photo="default.jpg")
            db.session.add(user)
            db.session.commit()
            print("Submitted without photo")
            return redirect(url_for("index"))
    return render_template("register.html", form =  form)





@app.route("/database")
def database():
    try:
        users =  User.query.all()
    except Exception as e:
        print(e)
        return render_template("database.html", empty = True)
    else:
        return render_template("database.html", users =  users)



@app.route("/delete/<int:userid>")
def delete_user(userid):
    user =  User.query.filter_by(id = userid).first()
    db.session.delete(user)
    db.session.commit()
    flash("User has been deleted", category = "danger")
    return redirect(url_for("database"))