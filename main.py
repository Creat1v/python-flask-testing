#!/usr/bin/python
# Based on https://pythonspot.com/login-authentication-with-flask/ and adjusted
"""Webserver via Flask for testing purpose"""

import os
from flask import Flask, flash, render_template, request, session

APP = Flask(__name__)


@APP.route('/')
def home():
    """Root page"""
    if not session.get('logged_in'):
        return render_template('login_test.html')

    return "Hello Boss! <a href='/logout'>Logout</a>"


@APP.route('/login', methods=['POST'])
def do_admin_login():
    """Login page/function"""
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return home()
        # return render_template('login_test.html')

    flash('wrong password!')
    return home()


@APP.route('/logout')
def logout():
    """Logout page/function"""
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    APP.secret_key = os.urandom(12)
    APP.run(debug=True, host='127.0.0.1', port=5000)
