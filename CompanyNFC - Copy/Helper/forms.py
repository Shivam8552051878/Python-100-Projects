from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from email_validator import validate_email

from wtforms.validators import DataRequired, URL


class RegisterationForm(FlaskForm):
    name = StringField(label="Full Name", name="name", validators=[DataRequired()])
    email = EmailField(label="Email", name="email", validators=[DataRequired()])
    password = PasswordField(label="Password", name="password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = EmailField(label="Email", name="email", validators=[DataRequired()])
    password = PasswordField(label="Password", name="password", validators=[DataRequired()])
    submit = SubmitField(label="Let me in.", name="submit")


class VCardFrom(FlaskForm):
    first_name = StringField(label="First Name", name="first_name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", name="last_name", validators=[DataRequired()])
    organization = StringField(label="Company Name")
    title = StringField(label="Job Profile")
    # photo_url = request.form['photo_url']
    work_phone = StringField(label="Work Phone No", name="work_phone")
    home_phone = StringField(label="Home Phone No", name="home_phone")
    cell_phone = StringField(label="Cell Phone No", name="cell_phone")
    whatsapp_number = StringField(label="Whatsup No", name="whatsapp_number")

    work_fax = StringField(label="Work Fax No", name="work_fax")
    work_email = StringField(label="Work Email", name="work_email")
    home_email = StringField(label="Home Email", name="home_email")
    website = StringField(label="Website URL", name="website")
    work_address = StringField(label="Work Address", name="work_address")
    home_address = StringField(label="Home Address", name="home_address")
    # birthday = request.form['birthday']
    # anniversary = request.form['anniversary']
    notes = StringField(label="About Company", name="notes")
    linkedin_profile = StringField(label="Linkedin URL", name="linkedin_profile")
    twitter_profile = StringField(label="Twitter URL", name="twitter_profile")
    facebook_profile = StringField(label="Facebook URL", name="facebook_profile")
    submit = SubmitField("Create VCard")
