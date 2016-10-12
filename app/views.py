import os
from app import app
from flask import Flask

@app.route('/')
@app.route('/home')
def home():
    return '<h1> Hey Shravan...!!!</h1><h2>Working fine now </h2>'

