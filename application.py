from flask import Flask
app = Flask(__name__)

@app.route("/")
def get(self):
     self.redirect("https://www.bigcommerce.com/", True)