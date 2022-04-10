# Import Form and RecaptchaField (optional)
from flask_wtf import Form  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import BooleanField, PasswordField, StringField, SubmitField

# Import Form validators
from wtforms.validators import DataRequired

from app.mod_auth.models import User


class RegisterForm(Form):
    username = StringField('Userna,e', [DataRequired(
        message='Whats the username?')])
    email = StringField('Email Address', [DataRequired(
        message='Forgot your email address?')])
    password = PasswordField('Password', [
        DataRequired(message='Must provide a password. ;-)')])

    def validate_on_submit(self):
        """
        :rtype: bool
        """
        email = User.query.filter_by(
            email=self.email.data.lower()).first()
        username = User.query.filter_by(
            username=self.username.data.lower()).first()
        if username:
            self.username.errors.append("That username is already taken")
            return False
        if email:
            self.email.errors.append("That email is already taken")
            return False
        return True
