# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField
# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField
# Import Form validators
from wtforms.validators import DataRequired


class BoardForm(FlaskForm):
    board_name = StringField('board_name', [DataRequired()])
