from flask import Flask, render_template

app = Flask(__name__)

dev=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def new():
    return render_template('dojos.html')

app.run(debug=dev)
