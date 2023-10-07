from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "Black Bananas"
a = []


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", daily=a)


@app.route("/create")
def create():
    text = request.args.get("text")
    a.append(text)
    return {"status": "OK", "text": text}


app.run(debug=True)
