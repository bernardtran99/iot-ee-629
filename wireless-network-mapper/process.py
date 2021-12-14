import sys
import time
import subprocess
import os

networkList = ()

result = subprocess.run(["sudo","iwlist","wlan0","scan"])
