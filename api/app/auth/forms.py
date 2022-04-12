# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField
# Import Form elements such as TextField and BooleanField (optional)
from wtforms import BooleanField, PasswordField, StringField, SubmitField
# Import Form validators
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email Address')
    password = StringField('Password')
    # submit = SubmitField('Submit')
