from flask import Flask, session, render_template, redirect, request

app = Flask(__name__)
app.secret_key = "thisissupersecret"

@app.route("/")
def index():
    if "miles" not in session:
        session["miles"] = 0
    return render_template("index.html")

@app.route("/walk", methods=["POST"])
def walk():
    if reqeust.form["back"]:
        session["miles"] += int(request.form["miles"])
    elif request.form["back"]:
        session["miles"] -= int(request.form["miles"])
    return redirect("/")

@app.route("/reset")
def reset():
    session["miles"] = 0
    return redirect("/")

app.run(debug=True)
