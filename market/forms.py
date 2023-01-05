from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User



class RegisterForm(FlaskForm):

  def validate_username(self, username_to_check):
    username_found = User.query.filter_by(username=username_to_check.data).first()
      
    if username_found: # if username is already existing
      raise ValidationError('Username already exists! Please try a different username')

  def validate_email_address(self, email_address_to_check): # if email address is already existing
    email_address_found = User.query.filter_by(email_address=email_address_to_check.data).first()

    if email_address_found:
      raise ValidationError('Email address is already exists! Please try a different email address')

  username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
  email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
  password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
  password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
  submit = SubmitField(label='Create Account')
  
class LoginForm(FlaskForm):
  username = StringField(label='User Name', validators=[DataRequired()])
  password = PasswordField(label='Password', validators=[DataRequired()])
  submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
  submit = SubmitField(label='Purchase Item!')

class SellItemform(FlaskForm):
  submit =SubmitField(label='Sell Item!')