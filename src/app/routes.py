from app import app
from flask import request

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/forecast')
def forecast():
    if not request.data:
        return "err"
    print(request.data)
    return request.data
.