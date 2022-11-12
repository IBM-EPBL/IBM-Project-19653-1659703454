from flask import Flask,redirect

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome to flask"

if __name__=='__main__':
    app.run(debug=True)