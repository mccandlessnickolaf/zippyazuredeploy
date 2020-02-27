from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://zippyloan.com/", code=302)
