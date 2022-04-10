# Import Form and RecaptchaField (optional)
from flask_wtf import Form  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import BooleanField, PasswordField, StringField, SubmitField

# Import Form validators
from wtforms.validators import DataRequired


# Define the login form (WTForms)

class LoginForm(Form):
    email = StringField('Email Address', [DataRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [
        DataRequired(message='Must provide a password. ;-)')])
