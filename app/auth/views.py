from flask import render_template
from . import auth
from .forms import LoginForm, RegisterForm
from flask_login import current_user


@auth.route('/login', methods=['GET', "POST"])
def login():
    form = LoginForm()
    """validation"""
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    """validation"""
    """"""
    return render_template('auth/register.html', form=form)
