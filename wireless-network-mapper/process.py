import sys
import time
import subprocess
import os
import re

networkList = ()


result = subprocess.Popen(["sudo","iwlist","wlan0","scan"],stdout=subprocess.PIPE)
output, error = result.communicate()

for line in output:
    if re.search("ESSID",line):
        print(line)