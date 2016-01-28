from flask import (render_template, redirect, url_for, abort,
                   flash, request, current_app, make_response, g)
from . import main
from .. webscraper import videos
from flask.ext.login import login_required, current_user


@main.before_request
def before_request():
    if not current_user:
        g.user = "Guest"
    else:
        g.user = current_user.get_id()


@main.route("/")
@login_required
def index():
    return render_template('index.html', user=g.user)


@main.route('/a', methods=['GET', 'POST'])
@login_required
def movie():
    if request.method == "POST":

        movies_list = videos.find_movie(request.form['search'])
        print(movies_list)

        return render_template(
            'index.html', movies_list=movies_list, url=None, user=g.user)

    else:
        return render_template('index.html', user=g.user)