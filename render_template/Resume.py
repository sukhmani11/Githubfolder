# %%

from flask import Flask
from flask import render_template, request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('resume.html')

    # interacting with html web pages


# %%
app.run()