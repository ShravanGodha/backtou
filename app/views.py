import os
from app import app
from flask import Flask

@app.route('/')
@app.route('/home')
def home():
    return '<h1> New SM created </h1>'

