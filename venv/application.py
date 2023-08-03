from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Good day! Ha Ha! Best Bike App!</h1></body></html>\n"