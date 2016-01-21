from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/a', methods=['GET', 'POST'])
def movie():
    return render_template('index.html', url=request.form['search'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)