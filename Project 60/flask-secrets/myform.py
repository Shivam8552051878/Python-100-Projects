from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from  wtforms.validators import DataRequired

class MyForm(FlaskForm):
    email = EmailField(validators=[DataRequired()], label="Email")
    name = StringField(validators=[DataRequired()], label="Name")
    password = PasswordField(validators=[DataRequired()], label="Password")
    submit = SubmitField(label="Log In")
