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
    products = products.replace('%20','')
    ServicesInfo = session.query(Services).filter_by(Name = products).all()
    print(ServicesInfo)
    Img = ServicesInfo[0][3]
    Title = ServicesInfo[0][1]
    ShortDesc = ServicesInfo[0][4]
    LongDesc = ServicesInfo[0][5]
    if ServicesInfo[0][6]:
        Contact = True
    else:
        Contact = False
    if ServicesInfo[0][7]:
        Price = True
    else:
        Price = False
    if ServicesInfo[0][8]:
        TFImg = True
    else:
        TFImg = False
    return render_template('ProductPage.html',info = ServicesInfo, Img = Img, Title = Title, ShortDesc = ShortDesc, LongDesc = LongDesc, Contact = Contact, Price = Price,TFImg = TFImg)

@app.route("/Contact_Us")
def Contact_Us():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)