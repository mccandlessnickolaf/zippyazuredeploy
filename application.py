from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    Flask.redirect("https://zippyloan.com/", True)
