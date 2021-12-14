import sys
import time
import subprocess
import os
import re
from datetime import datetime



network_list = {"ESSID":0}

times = 0

while times < 10:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    network_list["ESSID"] = current_time

    result = subprocess.Popen(["sudo","iwlist","wlan0","scan"],stdout=subprocess.PIPE, universal_newlines=True)
    output, error = result.communicate()

    for line in output.split("\n"):

        if re.search('Signal',line):
            signal = re.search('Signal level=(.*) dBm',line)
            signal_level = []
            signal_level = signal.group(1)
        
        if re.search('ESSID',line):
            essid = re.search('ESSID:"(.*)"',line)
            network_list[essid.group(1)] = signal_level
            # print(essid.group(1))

    print(network_list)
    print("\n")
    times += 1
    time.sleep(10)