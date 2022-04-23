from flask import Flask, render_template,request,flash,redirect,url_for,session
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
app = Flask(__name__)
app.secret_key="123"
#it is the database where all record and data table is stored ..

app.config['SQLALCHEMY_DATABASE_URI']      = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

Base = declarative_base()
#it is the user file of the data storing..
class users(db.Model):
    #it is the class system for returning the all data of the users and plot the function that defines all the users.

    id         =    db.Column(db.Integer , primary_key=True)
    username   =   db.Column(db.String(50), unique=True)
    fullname   =   db.Column(db.String(50))
    contact    =   db.Column(db.String(15))
    password   =   db.Column(db.String(50))
    repassword = db.Column(db.String(50))
    def __init__(self, username, fullname,contact,password,repassword):
        self.username   =   username
        self.fullname   =   fullname
        self.contact    =   contact
        self.password   =   password
        self.repassword =   repassword

class dataset(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120))
    address=db.Column(db.String(120))
    email=db.Column(db.String(120))
    contact=db.Column(db.Integer)
    password=db.Column(db.String(120))
    rpassword=db.Column(db.String(120))

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup' ,methods=["GET","POST"])

#it is the form data validation function
def signup():
    email=request.form.get('email')
    password=request.form.get('password')
    data=request.form.to_dict()
    data_csv(data)
    return "the email {} and password{}  ".format(email,password)
    
@app.route('/login_validation' ,methods=["GET","POST"])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    return "the email {} and password{}  ".format(email,password)


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        #It is the Login system and Model for logging inside the classroom for ..
        #it is the First requirements for the Email address. 
        username=request.form['username']
        password=request.form['password']
        data=users.query.filter_by(username=username).first()
        print(data.username)
        if data and data.password==password:
            return render_template("login.html")

        else:

            flash("Username and Password Mismatch","danger")

    return redirect(url_for("index"))
#it is the form

@app.route('/validation',methods=["GET","POST"])
def validation():
    email=request.form.get('email')
    password=request.form.get('password')
    return "the email {} and password{}  ".format(email,password)


@app.route('/login',methods=["GET","POST"])
def customer():
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    #it is the function for finding the data inside the tables and databse.

    if request.method=='POST':
        username="hemantmishra"
        q1=users.query.filter_by(username=username).first()
        print(q1.username)
        print(q1.fullname)
        print(q1.password)
        try:
            #there is the a lot of the parameters --> for the collection 
            #it is the database table that holds the details of the each user.
            #t
            username   =    request.form['username']
            fullname   =    request.form['fullname']
            contact    =    request.form['contact']
            password   =    request.form['password']
            repassword =    request.form['repassword']
            print(contact)
            new_data = users(username=username,fullname=fullname,contact=contact,password=passsword,repassword=repassword)
            #data object is added inside the database.. 
            db.session.add(new_data)
            #it is commited to the database.instance is now save inside the databse.
            db.session.commit()
            print(new_data.username)
            print(new_data.fullname)
            flash("Record Added  Successfully","success")
        except:

            flash("Error in Insert Operation","danger")
            
        finally:
            return redirect(url_for("index"))
            
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == '__main__':

    app.run(debug=True)
