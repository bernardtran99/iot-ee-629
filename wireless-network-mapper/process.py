import sys
import time
import subprocess
import os

networkList = ()


reuslt = subprocess.Popen(["sudo","iwlist","wlan","scan"],stdout=subprocess.PIPE, universal_newlines=True)
output, error = result.communicate()