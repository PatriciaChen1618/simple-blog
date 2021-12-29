from flask import render_template, session, flash, redirect, url_for
from . import main
from .forms import NameForm


@main.route('/')
def index():  # render index.html
    return render_template("index.html")


@main.route('/user', methods=['GET', 'POST'])
def user():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('You changed name!')
        session['name'] = form.name.data
        return redirect(url_for('main.user'))
    return render_template("user.html", form=form, name=session.get('name'))