from flask import (render_template, redirect, url_for, abort,
                   flash, request, current_app, make_response)
from . import main
from flask.ext.login import login_required, current_user


@main.route("/")
@login_required
def index():
    return render_template('index.html')


@main.route('/a', methods=['GET', 'POST'])
def movie():
    return render_template('index.html', url=request.form['search'])