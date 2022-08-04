from flask import request, render_template, redirect, url_for, flash
from market import app, db
from market.models import Product, User
from market.forms import RegisterForm, LoginForm, RemoveItemForm, UpdateQtyForm, AddProductForm, SMSForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
import vonage

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market",methods=['GET','POST'])
@login_required
def market_page():
        
    updateQtyForm = UpdateQtyForm()
    if updateQtyForm.validate_on_submit():
        update_item = request.form.get('updated_item')
        update_item_object = Product.query.filter_by(id=update_item).first()
        if update_item_object:
            update_item_object.quantity = updateQtyForm.new_quantity.data
            db.session.commit()
            flash(f'{update_item_object.product_name} quantity has been updated successfully! ', category='success')
        return redirect(url_for('market_page'))

    removeItemForm = RemoveItemForm()
    if removeItemForm.validate_on_submit():
        remove_item = request.form.get('removed_item')
        remove_item_object = Product.query.filter_by(id=remove_item).first()
        db.session.delete(remove_item_object)
        db.session.commit()
        flash(f'{remove_item_object.product_name} has been removed from product list! ', category='info')
        return redirect(url_for('market_page'))


    products = Product.query.all() 
    return render_template("market.html",products=products, removeItemForm=removeItemForm, updateQtyForm=updateQtyForm)


@app.route("/register", methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password_hash=generate_password_hash(form.password1.data, method='sha256'))

        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are logged in as {user_to_create.username} ', category='success')

        return redirect(url_for('market_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/addProduct', methods=['GET', 'POST'])
def product_page():
    addProductForm = AddProductForm()
    if addProductForm.validate_on_submit():
        product_to_create = Product(product_name=addProductForm.product_name.data, product_price=addProductForm.product_price.data, quantity = addProductForm.quantity.data, supplier = addProductForm.supplier.data)
        db.session.add(product_to_create)
        db.session.commit()
        flash(f'Product created successfully!', category='success')
        return redirect(url_for('market_page'))
    
    if addProductForm.errors != {}:
        for err_msg in addProductForm.errors.values():
            flash(f'There was an error with creating the product: {err_msg}', category='danger')
    return render_template('addProduct.html', addProductForm=addProductForm)

@app.route('/sendSMS/<int:product_id>', methods=['GET', 'POST'])
def send_SMS(product_id):
    # SMSFORM SECTION
    smsForm = SMSForm()
    client = vonage.Client(key="23ea4213", secret="PeAdOvf4mMJ0U367")
    sms = vonage.Sms(client)
    if request.method == 'POST':
        # item = request.form.get('item')
        item_object = Product.query.filter_by(id=product_id).first()
        phone = smsForm.phone_number.data
        message = f'{item_object.product_name} is out of stock!'
        print('Landing Phone Number is: ', phone)
        print(message)

        responseData = sms.send_message(
            {
                "from": "MENLOBEN",
                "to": phone,
                "text": message,
            }
        )

        if responseData["messages"][0]["status"] == "0":
            flash(f'Message has been successfully sent to {phone}.', category="success")
        else:
            flash(f"Message failed with error: {responseData['messages'][0]['error-text']}", category='danger')

        return redirect(url_for('market_page'))
    
    return render_template('sms.html', smsForm = smsForm)
@app.route('/login', methods=['GET','POST'])
def login_page():

    form = LoginForm()
    if form.validate_on_submit():

        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and check_password_hash(attempted_user.password_hash, form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as  {attempted_user.username} ', category='success')
            return redirect(url_for('market_page'))

        else:
            flash('Username and password do not match! Please try again', category='danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))