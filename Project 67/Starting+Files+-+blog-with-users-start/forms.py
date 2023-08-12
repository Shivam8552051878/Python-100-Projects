from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from email_validator import validate_email

from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterationForm(FlaskForm):
    name = StringField(label="Full Name", name="name", validators=[DataRequired()])
    email = EmailField(label="Email", name="email", validators=[DataRequired()])
    password = PasswordField(label="Password", name="password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = EmailField(label="Email", name="email", validators=[DataRequired()])
    password = PasswordField(label="Password", name="password", validators=[DataRequired()])
    submit = SubmitField(label="Let me in.", name="submit")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
