from typing import ItemsView
from app import db, login 
from sqlalchemy.sql import func
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
# from flask_mail import Message

class user_account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    phone_number = db.Column(db.String(16), unique=True)
    password_hash = db.Column(db.String(128))
    # orders = db.relationship('order', backref='user_account', lazy=True)
    
    email_auth_codes = db.relationship('user_email_auth', backref='user_account', lazy=True)
    #create timestamps, accounts for server latency by using server timestamps
    time_created = db.Column(db.TIMESTAMP, server_default=func.now())
    time_updated = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# use to pass current user to current page    
@login.user_loader
def load_user(id):
    return user_account.query.get(int(id))   

class user_email_auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_account_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    url_hash = db.Column(db.String(120), nullable=False)
    time_created = db.Column(db.TIMESTAMP, server_default=func.now())

    def set_url_hash(self):
        self.url_hash = secrets.token_urlsafe(16)
        # call auth email logic from here, never will set a hash without wanting an email sent
        #send_validation_email = Message("Hello", recipients=[self.id])    
    
#TODO setup menu/ordering system    
#
# class user_order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_account_id = db.Column(db.Integer, db.ForeignKey('user_account.id'))
#     menu_items = db.relationship('menu_item', backref='user_order', lazy=True)


#     id = db.Column(db.Integer, primary_key=True)
#     user_order_id = db.Column(db.Integer, db.ForeignKey('user_order.id'))
    
#     def __repr__(self):
#         return '<User {}>'.format(self.username)   
    
# class menu(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_account_id = db.Column(db.Integer, db.ForeignKey('user_account.id'))
#     item_title =   
#     item_price = 
#     item_amount = 
#     def __repr__(self):
#         return '<User {}>'.format(self.username)   
    
    