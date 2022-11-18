from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadimage')
def uploadimage():
    return render_template('uploadimage.html')

@app.route('/viewhistory')
def viewhistory():
    return render_template('viewhistory.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)