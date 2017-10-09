from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def validation():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(request.form['name']) < 1:
        flash('please put your name')
    elif len(request.form['comment']) > 120:
        flash('comment cannot exceed 120 characters')
    else:
        flash('Success!')
    return render_template('result.html')


app.run(debug=True)
