from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, FloatField, IntegerField, DateField
from wtforms.validators import Email,Length,EqualTo, DataRequired, ValidationError
from market.models import User, Product
class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
        
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Please try a different email address')
    
    username = StringField(label='Username:', validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class RemoveItemForm(FlaskForm):
    submit = SubmitField(label='Remove Item!')

class UpdateQtyForm(FlaskForm):
    new_quantity = StringField(label='Update Product:', validators=[DataRequired()])
    submit = SubmitField(label='Update Item!')

class AddProductForm(FlaskForm):

    def validate_product_name(self, product_to_check):
        product = Product.query.filter_by(product_name=product_to_check.data).first()
        if product:
            raise ValidationError('Product already exists! Please add a different product')
        
    product_name = StringField(label='Product Name:', validators=[Length(min=2,max=30), DataRequired()])
    product_price = FloatField(label='Product Price:', validators=[DataRequired()])
    quantity = IntegerField(label='Product Quantity:', validators=[DataRequired()])
    supplier = StringField(label='Name of Supplier:', validators=[DataRequired()])
    submit = SubmitField(label='Add Product')

class SMSForm(FlaskForm):
    phone_number = StringField(label='Phone Number:', validators=[Length(min=9,max=9), DataRequired()])
    submit = SubmitField(label='Send SMS')