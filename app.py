#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def ant():
    return 'Ameisenscheisse\n'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

