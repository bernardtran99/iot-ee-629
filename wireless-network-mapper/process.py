import sys
import time
import subprocess
import os
import re

network_list = {}


result = subprocess.Popen(["sudo","iwlist","wlan0","scan"],stdout=subprocess.PIPE, universal_newlines=True)
output, error = result.communicate()

for line in output.split("\n"):
    if re.search('ESSID',line):
        essid = re.search('ESSID:"(.*)"',line)
        network_list[essid.group(1)] = 0
        # print(essid.group(1))

print(network_list)