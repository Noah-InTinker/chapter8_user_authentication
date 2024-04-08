from app import app, db
from app.models import User
from flask import render_template, flash, redirect
from app.forms import RegisterForm, AddProductForm, LoginForm
from flask_login import login_user, logout_user, login_required


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@app.route('/index')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')


@app.route('/about-me')
def about_me():
    """About me URL"""
    return render_template('about_me.html', title='about me page')


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Product URL"""
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'Your product has been saved {form.product_name.data}')
        return redirect('/index')
    return render_template('add_product.html', title='Add Product', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to register as {form.username.data}')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_pasword(form.password.data):
            flash('Invalid username or password')
            return redirect('index')
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)