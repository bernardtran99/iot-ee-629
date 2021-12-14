import sys
import time
import subprocess
import os
import re

networkList = ()


result = subprocess.Popen(["sudo","iwlist","wlan0","scan"],stdout=subprocess.PIPE, universal_newlines=True)
output, error = result.communicate()

for line in output.split("\n"):
    if re.search("ESSID",line):
        print(line)