# Import Form and RecaptchaField (optional)
from flask_wtf import Form  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import BooleanField, PasswordField, StringField, SubmitField

# Import Form validators
from wtforms.validators import Required, Email


# Define the login form (WTForms)

class LoginForm(Form):
    email = StringField('Email Address', [Email(),
                                          Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
        Required(message='Must provide a password. ;-)')])
