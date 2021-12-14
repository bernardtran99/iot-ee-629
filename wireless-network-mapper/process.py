import sys
import time
import subprocess
import os

networkList = ()

result = subprocess.run(["sudo","iwlist","wlan0","scan","|","grep","-e","Quality","-e","ESSID"])
