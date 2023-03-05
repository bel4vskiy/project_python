from flask import Flask, redirect, render_template, request, url_for
from pars import Parser

app = Flask(__name__)



@app.route('/',methods = ['POST', 'GET'])
def login():
    user = request.args.get('login')
    password = request.args.get('psw')
    if user == "pobeda" and password == "yes":
        access = True
        return redirect("pars")
    return render_template("login.html")

@app.route('/pars')
def parser():
    a = Parser()
    return render_template("site.html", a=a)


if __name__=="__main__":
    app.run(debug = True)
