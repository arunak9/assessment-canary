# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>This is Aruna Sri Priya</h1><h2 style='color: #ffef00; text-shadow: 2px 2px 3px #030000'>Canary Version</h2></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)