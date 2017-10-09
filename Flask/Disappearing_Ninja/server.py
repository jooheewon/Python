from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def all_ninjas():
    return render_template('group.html')

@app.route('/ninja/<color>')
def color_ninja(color):

    print color
    color = color.lower()
    if color == 'default':
        ninja = url_for('static', filename='img/tmnt.png')
        return render_template('ninja.html', image =ninja, ninja_pic ="Group Photo")
    elif color == 'blue':
        ninja = url_for('static', filename='img/leonardo.jpg')
        return render_template('ninja.html', image =ninja, ninja_pic ="Leonardo")
    elif color == 'orange':
        ninja = url_for('static', filename='img/michelangelo.jpg')
        return render_template('ninja.html', image =ninja, ninja_pic ='Michelangelo')
    elif color == 'red':
        ninja = url_for('static', filename='img/raphael.jpg')
        return render_template('ninja.html', image =ninja, ninja_pic ='Raphael')
    elif color == 'purple':
        ninja = url_for('static', filename='img/donatello.jpg')
        return render_template('ninja.html', image =ninja, ninja_pic ='Donatello')
    else:
        notfound = url_for('static', filename='img/notapril.jpg')
        return render_template('ninja,html', image =notfound, ninja_pic ='no ninja')

app.run(debug = True)
