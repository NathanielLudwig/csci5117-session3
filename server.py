from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hi', methods=['GET'])
def hi():
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name)


@app.route('/fans', methods=['GET'])
def fans():
    return render_template('fans.html')