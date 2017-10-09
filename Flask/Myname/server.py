from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def your_name():
    print request.form
    return redirect ('success.html')

app.run(debug=True)
