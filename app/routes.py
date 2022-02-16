from flask import request, render_template, flash, redirect, url_for
import json
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import user_account, user_email_auth
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/<user>')
def index(user="default user"):
    return render_template('index.html', user_val=user) 

@login_required
@app.route('/api/', methods=['POST'])
def post():
    value = json.loads(request.data)
    return json.dumps(value)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # creates login form object, validate_on_submit will only run on submit() POST within login.html
    # validate_on_submit checks user form against form and returns errors/ends request if validation fails
    # GET requests return false and login.html is rendered and returned
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # check if user_account record with this email exists and user password_hash matched
        user = user_account.query.filter_by(email=login_form.email.data).first()
        if user is None or not user.check_password(login_form.password.data):
            #flash passes data into next request
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        # next page checks to see if user was redirected to login and returns them if so
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        new_user = user_account(email=register_form.email.data)
        new_user.set_password(register_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        new_email_auth = user_email_auth(user_account_id=new_user.id)
        new_email_auth.set_url_hash()
        db.session.add(new_email_auth)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=register_form)

@app.route('/logout')
def logout():
    logout_user()
    flash('User Logged Out')
    return redirect(url_for('index'))


#TODO setup other pages
# @app.route('/home/', methods=['POST'])
# def ():
#     return render_template('index.html')

# @app.route('/about/', methods=['POST'])
# def post():
#     return render_template('about.html')

# @app.route('/about/', methods=['POST'])
# def post():
#     return render_template('about.html')

# @app.route('', methods=['POST'])
# def post():
#     value = json.loads(request.data)
#     return json.dumps(value)
