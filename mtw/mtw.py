from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/a', methods=['GET', 'POST'])
def movie():
    return render_template('index.html', url=request.form['search'])
