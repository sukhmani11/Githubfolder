# %%
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<a href = http://127.0.0.1:5000/quickstart> Quickstart<a> '+ '<a href = http://127.0.0.1:5000/LearnPython> LearnPython<a> '
@app.route('/quickstart')
def quickstart():
    return 'Hello, Quick!'
@app.route('/LearnPython')
def quicktostart():
    return render_template('Student.html')

# %%

from flask import Flask
from flask import render_template, request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('Student.html')

    # interacting with html web pages
@app.route('/input',methods=['POST', 'GET'])  # There are two methods to transfer data from client browser to the web server
@app.route('/test')
def test():
    if request.method == 'POST':  # if data is recieved from the form....
         ht = int(request.form['height'])
         age = int(request.form['age'])
         print(ht,age)
    return render_template('resume.html')

# %%
app.run()

# %%
# interacting with html web pages
@app.route('/input',methods=['POST', 'GET'])  # There are two methods to transfer data from client browser to the web server
def test():
    if request.method == 'POST':  # if data is recieved from the form....
         ht = int(request.form['height'])
         age = int(request.form['age'])
         print(ht,age)
    return render_template('test.html')



# %%
