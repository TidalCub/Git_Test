from re import DEBUG
from flask import Flask, request, render_template, redirect

from DBModules import Services, session 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Expiriance")
def Expiriance():
    return redirect('/')


@app.route("/Services")
def ServicesFunc():
    ServicesInfo = session.query(Services).all()
    print(len(ServicesInfo))
    for i in ServicesInfo:
        print(i[3])
    return render_template('Services.html',Services=ServicesInfo)


@app.route("/Services/<products>")
def ServicesProducts(products):
    return render_template('ProductPage.html')

@app.route("/Contact_Us")
def Contact_Us():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)