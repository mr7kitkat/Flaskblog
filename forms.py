from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class BaseForm(FlaskForm):
  username = StringField('username', validators=[DataRequired(),Length(min=4,max=20)])
  password = PasswordField('password', validators=[DataRequired(), Length(min=4, max=20)])
  
  
class RegistrationForm(BaseForm):
  email = EmailField('email', validators=[DataRequired()])
  confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
  sign_up = SubmitField('sign up')
  
class LoginForm(BaseForm):
  remember_me = BooleanField()
  login = SubmitField('login')
  
  
