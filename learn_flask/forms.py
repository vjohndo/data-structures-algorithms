from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# This will inherit from the Flask Form
class RegistrationForm(FlaskForm):

    # A string field, is an object to be imported from the wtforms module
    # First arg = name of the field, and will be used in html
    # Second arg = we want user name to min amd max limit --> use validators, classes that we can import

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):

    # A string field, is an object to be imported from the wtforms module
    # First arg = name of the field, and will be used in html
    # Second arg = we want user name to min amd max limit --> use validators, classes that we can import
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")

    # Need to set a secret key