from billApp import app
from flask import render_template,redirect,url_for,request,session
from billApp.models import Item, Customer
from billApp import db


@app.route("/h")
def home():
    data = {}
    data['customer'] = "San"
    print(data)
    return render_template("home.html",data=data)



@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price1 = request.form['price1']
        price2 = request.form['price2']
        price3 = request.form['price3']
        pcode = request.form['pcode']
        new_item = Item(name=name, price1=price1, price2=price2, price3=price3, pcode=pcode)

        try:
            db.session.add(new_item)
            db.session.commit()
        except:
            return 'There was an issue adding your task'
    return render_template('item.html')

@app.route('/',methods=['POST', 'GET'])
def customer():
    if request.method == 'POST':
        vid = request.form['cid']
        kid = db.session.query(Customer.query.filter(Customer.cid == vid).exists()).scalar()
        if kid:
            print(vid)
            print(kid)
            data = {}
            data["customer"] = "San"
            session['data'] = data
            return redirect(url_for("home",data=data))
        else:
            print("error")
    return render_template('customer.html')

@app.route('/g',methods=['POST','GET'])
def guest():
    data = {}
    data["customer"] = ""
    return render_template('guest.html',data = data)

@app.route('/register',methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        cid = request.form['cid']
        name = request.form['name']
        number = request.form['number']
        new_c = Customer(cname=name, cid=cid, number=number)
        try:
            db.session.add(new_c)
            db.session.commit()
            return redirect(url_for('home'))
        except:
            return 'There was an issue adding your task'
    return render_template('register.html')

