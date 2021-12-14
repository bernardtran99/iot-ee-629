
#Wireless Network Mapper
#Bernard Tran

import sys
import time
import subprocess
from flask import Flask

network_dict = {}

app = Flask(__name__)

@app.route("/")
def web_page():
    return "Starting app..."

if __name__ == "__main__":
    app.run(0.0.0.0)