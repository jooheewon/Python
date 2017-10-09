from flask import Flask, render_template

app = Flask(__name__)

dev=True

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=dev)
