import sys
import time
import subprocess
import os

networkList = ()


result = subprocess.Popen(["sudo","iwlist","wlan0","scan"],stdout=subprocess.PIPE, universal_newlines=True)
output, error = result.communicate()

print(output)