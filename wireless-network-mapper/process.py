import sys
import time
import subprocess
import os
import re

network_list = {}


result = subprocess.Popen(["sudo","iwlist","wlan0","scan"],stdout=subprocess.PIPE, universal_newlines=True)
output, error = result.communicate()



for line in output.split("\n"):
    signal_level = 0
    if re.search('Signal level',line):
        signal = re.search('Signal level=(.*) dbm',line)
        signal_level = signal.group(1)
    if re.search('ESSID',line):
        essid = re.search('ESSID:"(.*)"',line)
        network_list[essid.group(1)] = signal_level
        # print(essid.group(1))

print(network_list)