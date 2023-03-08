from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index01.html')

@app.route('/products')
def Intro():
    return "This page gives Intro about Products"

@app.route('/products/info')
def info():
    return "this Page gives Info about our products"

if __name__=="__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')