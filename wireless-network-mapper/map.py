
#Wireless Network Mapper
#Bernard Tran

import sys
import time
import subprocess
from flask import Flask, redirect, url_for, request

network_dict = {}

app = Flask(__name__)

@app.route("/")
def index():
    html_raw = "<h1>Wireless Network Mapper</h1>"
    return render_template('table.html')

if __name__ == "__main__":
    app.run("0.0.0.0")