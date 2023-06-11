from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='USERNAME:')
    email_address = StringField(label='EMAIL:')
    password1 = PasswordField(label='PASSWORD:')
    password2 = PasswordField(label='CONFIRM PASSWORD:')
    submit = SubmitField(label='Create Account')