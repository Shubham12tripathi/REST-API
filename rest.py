from Application import app,db
from flask import render_template,request,url_for,redirect
from datetime import datetime
from Application.models import User


@app.route("/data", methods=['POST'])
def data():
    if request.method == "POST":
        firstname= request.form['fname']
        middlename= request.form['mname']
        lastname= request.form['lname']
        phone= request.form['phone']
        email= request.form['email']
        gender= request.form['gender']
        DOB=datetime.strptime(request.form['dob'],'%Y-%m-%d')
        Education=request.form['Education']
        address= request.form['address']
        Skill=request.form['Skill']
        CurrentDate=datetime.strptime(request.form['date'],'%Y-%m-%d')
        user= User(firstname,middlename,lastname,phone,email,gender,DOB,Education,address,Skill,CurrentDate)
        db.session.add(user)
        db.session.commit()
    return  redirect(url_for('userList') )


  
@app.route("/items", methods=["POST"])
def more():
    id_items=request.form['items']
    items=User.query.filter_by(id=id_items).all()
    return render_template("Detail.html", items= items[0] )