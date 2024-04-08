
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddProductForm(FlaskForm):
    """Product Form"""
    product_name = StringField('Product Name', validators=[DataRequired(), Length(1, 63)])
    product_description = TextAreaField('Product Description', validators=[DataRequired()])
    stock_available = SelectField('Stock Available', choices=[
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
    ])
    submit = SubmitField('Add Product')
    
    

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('username', validators=[DataRequired(), Length(1, 63)])
    email = StringField('email', validators=[DataRequired(), Length(1, 63), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Register')



class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('username', validators=[DataRequired(), Length(1, 63)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')