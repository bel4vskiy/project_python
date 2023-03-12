from flask import Flask, redirect, render_template, request, url_for
from pars import Parser

app = Flask(__name__)



@app.route('/',methods = ['POST', 'GET'])
def login():
    user = request.args.get('login')
    password = request.args.get('psw')
    if user == "pobeda" and password == "yes":
        access = True
        return redirect("csgo")
    return render_template("login.html")

@app.route('/csgo')
def parser_csgo():
    a = Parser()
    return render_template("csgo.html", a=a)


@app.route('/dota2')
def parser_dota():
    a = Parser()
    return render_template("dota.html", a=a)

@app.route('/rust')
def parser_rust():
    a = Parser()
    return render_template("rust.html", a=a)



if __name__=="__main__":
    app.run(debug = True)
