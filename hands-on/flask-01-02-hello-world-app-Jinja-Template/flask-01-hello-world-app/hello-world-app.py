from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello World!"    

@app.route('/second')
def second():
    return "This is the second page"

@app.route('/third/subthird')
def third():
    return "This is the third page"

@app.route('/fourth/<string:id>')
def fourth(id):
    return f"This is the fourth page with id: {id}"


