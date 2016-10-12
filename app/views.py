import os
from app import app
from flask import Flask

@app.route('/')
@app.route('/home')
def home():
    return '<h1> Hey Shravan...!!!</h1><h2>How r u Working tody</h2>'

