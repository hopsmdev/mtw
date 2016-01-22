from mtw import app, mongo
from flask import request, render_template, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required
from .forms import LoginForm
from .models import UserLogin


@app.route("/")
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.findOne({'email': form.email.data})

        if user and UserLogin.validate_login(user['password'], form.password.data):
            user_obj = UserLogin(user['email'])
            login_user(user_obj)
            return redirect(request.args.get("next") or url_for("index"))
    return render_template('login.html', title='Login', form=form)


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/a', methods=['GET', 'POST'])
def movie():
    return render_template('index.html', url=request.form['search'])