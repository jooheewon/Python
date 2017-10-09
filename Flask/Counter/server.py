from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html', count=session['count'])

@app.route('/inclement', methods=['POST'])
def inclement():
    session['count'] += 2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
