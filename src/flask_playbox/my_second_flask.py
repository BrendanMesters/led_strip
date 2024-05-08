
from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # loads the html file in ./templates/name.html
    status = "We just prepended a status to an otherwise static html file, woop!"
    return f'<p>{status}</p>\n' + render_template('hello.html', name=name)
