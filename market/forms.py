from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='USERNAME:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='EMAIL:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='PASSWORD:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='CONFIRM PASSWORD:', validators=[EqualTo('password1')])
    submit = SubmitField(label='Create Account')