#!/usr/bin/python
"""Webserver via Flask to test the webserver"""

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name = user)


if __name__ == '__main__':
    app.run(debug=True)
