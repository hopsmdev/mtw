from flask import request, render_template, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required
from .forms import LoginForm
from . import auth

from ..models.user import User


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():

        user = User.get_user(email=form.email.data)

        print("Loaded user: {}".format(user['email']))

        if user and User.verify_password(user['password'], form.password.data):
            login_user(User(user['email']), form.remember_me)
            return redirect(request.args.get("next") or url_for("main.index"))
    else:
        print("Cannot validate for user {}/{}".format(form.email.data, form.password.data))

    return render_template('auth/login.html', form=form)