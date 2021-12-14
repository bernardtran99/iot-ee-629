import sys
import time
import subprocess
import os

networkList = ()

result = subprocess.run(["ls","-l"])
