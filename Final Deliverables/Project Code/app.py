from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
from flask_mail import Mail, Message
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=cpw37068;PWD=5ojUnutmJuICfdAU",'','')

app = Flask(__name__)
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nutritiz5@gmail.com'
app.config['MAIL_PASSWORD'] = 'Nutrihealth '
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) # instantiate the mail class

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message=request.form['message']
        subject = request.form['subject']
        message= Message(subject,recipients=["nutritiz5@gmail.com"])
        message.sender = email
        message.body = message
        mail.send(message)
        success="Message sent"
        return render_template("result.html",success=success)


@app.route('/')


def login():
    return render_template('login.html')

@app.route('/login.html',methods = ['POST'])

def getUser():
    if request.method == 'POST':
        global message
        user = request.form['uemail']
        password = request.form['upwd']
        sql = "SELECT * FROM USERS where Email = ?"
        stmt = ibm_db.prepare(conn, sql)
        email = user
        # Explicitly bind parameters
        ibm_db.bind_param(stmt, 1,user)
        ibm_db.execute(stmt)
        dictionary = ibm_db.fetch_assoc(stmt)
        pwd = dictionary["PASSWORD"]
        if password != password:
            return render_template('error.html')
        
        return render_template('index.html')
    

@app.route('/register.html')

def putUser():
    return render_template('register.html')   

@app.route('/register.html',methods = ['POST'])

def storedUser():
    if request.method == 'POST':
        global message
        username = request.form['username']
        useremail = request.form['useremail']
        userphoneno = request.form['userphoneno']
        userpassword = request.form['userpassword']

        res = username + useremail + userphoneno + userpassword

        sql = "INSERT INTO USERS(Name,Email,Phonenumber,Password) VALUES(?,?,?,?);"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, useremail)
        ibm_db.bind_param(stmt, 3, userphoneno)
        ibm_db.bind_param(stmt, 4, userpassword)
        ibm_db.execute(stmt)
    return render_template('login.html')


def index():
    return render_template('index.html')

@app.route('/uploadimage')
def uploadimage():
    return render_template('uploadimage.html')

@app.route('/contactus')
def viewhistory():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True )