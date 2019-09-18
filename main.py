#!/usr/bin/python
# Based on https://pythonspot.com/login-authentication-with-flask/ and adjusted
"""Webserver via Flask for testing purpose"""

from flask import Flask, flash, redirect, render_template, request, session, abort
import os

APP = Flask(__name__)


@APP.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login_test.html')
    else:
        return "Hello Boss! <a href='/logout'>Logout</a>"


@APP.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return home()
        # return render_template('login_test.html')
    else:
        flash('wrong password!')
        return home()


@APP.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    APP.secret_key = os.urandom(12)
    APP.run(debug=True, host='127.0.0.1', port=5000)