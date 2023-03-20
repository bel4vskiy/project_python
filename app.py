from flask import Flask, redirect, render_template, request, url_for
from pars import Parser
from datab import MyDB
d = MyDB()

app = Flask(__name__)



@app.route('/log',methods = ['POST', 'GET'])
def login():
    user = request.form.get('login')
    password = request.form.get('psw')
    if (user is not None) and (password is not None):
        if d.check_access(user, password):
            return redirect("csgo")
    return render_template("login.html")

@app.route('/auth', methods = ['POST', 'GET'])
def auth():
    if request.method == 'GET':
        user = request.args.get('login')
        password = request.args.get('psw')
        if (user is not None) and (password is not None):
            if d.add_user(user, password):
                return redirect("/log")
    return render_template("auth.html")

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
