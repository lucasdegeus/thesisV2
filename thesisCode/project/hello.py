from flask import Flask, session, redirect, url_for, request
from markupsafe import escape
from flask import render_template


app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('test.html', name=name)
    return render_template('test.html', name=name)



@app.route('/text')
def hello_world():
    f = open("test.rtf", "r")
    return(escape(f.read()))



@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        return (request.form['description'])
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('test2.html', error=error)