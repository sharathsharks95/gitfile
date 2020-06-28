from flask import Flask

app = Flask(__name__)
@app.route("/home")
def home():
    return "Hello! this is the main page <h1>Hello</h1> "

if __name__=="___main__":
    app.run()