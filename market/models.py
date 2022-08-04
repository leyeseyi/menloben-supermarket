from market import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=120), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(length=30), nullable=False, unique=True)
    product_price = db.Column(db.Integer(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    supplier = db.Column(db.String(length=1024), nullable=False)

    @property
    def prettier_price(self):
        if len(str(self.product_price)) >= 4:
            return f'{str(self.product_price)[:-3]},{str(self.product_price)[-3:]}'

        else:
            return f'{self.product_price}'

    