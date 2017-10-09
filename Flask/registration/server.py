from flask import Flask, render_template, redirect, request, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def register():
    if len(request.form['firstname']) < 1:
        flash('please fill the blank')
    elif len(request.form['lastname']) < 1:
        flash('please fill the blank')
    elif len(request.form['password1']) < 8:
        flash('password must be longer than 8 characters')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash('success!')
        return redirect('result.html')

app.run(debug=True)
