from re import DEBUG
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Expiriance")
def Expiriance():
    return redirect('/')

@app.route("/Services")
def Services():
    return redirect('/')

@app.route("/Contact_Us")
def Contact_Us():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)