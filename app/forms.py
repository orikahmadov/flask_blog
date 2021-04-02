from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, \
    SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, InputRequired
from flask_wtf.file import  FileField, FileAllowed
from wtforms.fields.html5 import EmailField, DateField
from app import countries


class RegisterForm(FlaskForm):
    """Validators"""
    name  =  StringField("Your name ", validators=[Length(min=1, max = 40), DataRequired()])
    email =  EmailField("Your email", validators=[Email(), DataRequired()])
    birthday =  DateField("Your birthday ", validators=[DataRequired()], format= "%Y-%m-%d")
    gender  =  SelectField("Select your gender", validators=[DataRequired()], choices=["Male", "Female"])
    password =  PasswordField("Your password", validators=[DataRequired()])
    nationality =  SelectField("Nationality", choices=[name for name in countries])
    accept_terms =  BooleanField("Accepting all the terms", validators=[DataRequired("Please accept terms ")])
    message =  TextAreaField("Your story", validators=[Length(min=-1, max=300)])
    photo =  FileField("Upload your image", validators=[FileAllowed(["jpeg", "jpg", "png"])])
    submit = SubmitField("Send Application ")



