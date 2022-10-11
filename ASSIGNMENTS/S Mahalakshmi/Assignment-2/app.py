from flask import Flask, render_template
  
app = Flask(_name_)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signin")
def signin():
    return render_template('signin.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/about")
def about():
    return render_template('about.html') 


if _name_ == '_main_':
    app.debug = True
    app.run()