import sys
import time
import subprocess

networkList = ()

result = subprocess.run(['sudo iwlist' ], stdout=subprocess.PIPE).decode('utf-8')

print(result)