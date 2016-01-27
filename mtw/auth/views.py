from flask import request, render_template, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required
from .forms import LoginForm
from . import auth

from ..models import user


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():

        _user = user.get_user(email=form.email.data)

        print("------>> {}: {}".format(_user.get('email'), _user.get('password')))

        if _user and user.UserLogin.validate_login(
                _user['password'], form.password.data):

            user_obj = user.UserLogin(_user['email'])
            login_user(user_obj, form.remember_me)
            return redirect(request.args.get("next") or url_for("main.index"))
    else:
        print("Cannot validate for user {}/{}".format(form.email.data, form.password.data))

    return render_template('auth/login.html', form=form)