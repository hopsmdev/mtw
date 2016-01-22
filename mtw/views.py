from mtw import app
from flask import request, redirect, render_template, url_for


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/a', methods=['GET', 'POST'])
def movie():
    return render_template('index.html', url=request.form['search'])