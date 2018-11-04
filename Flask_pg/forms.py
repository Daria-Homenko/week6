from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired


class LoginForms(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class Sign_inForm(FlaskForm):
    s_username = StringField('Username', validators=[DataRequired()])
    s_age = StringField('Age', validators=[DataRequired()])
    s_email = StringField('Email', validators=[DataRequired()])
    s_password = PasswordField('Password', validators=[DataRequired()])
    s_submit = SubmitField('Sign in')