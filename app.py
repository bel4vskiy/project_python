from flask import Flask
from pars import Parser

app = Flask(__name__)


@app.route('/')
def hello():
    a = Parser()
    html = f'''
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TRADEBUFF</title>
    <link rel="stylesheet" href="static\style.css">

</head>

<body>
    <div class="grid">
        {a.sorted()}
    </div>
</body>

</html>
    '''
    return html



if __name__=="__main__":
    app.run(debug=True)
