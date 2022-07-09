#import needed Libraries
import os
import datetime
import sys
import re

file = open("arpTable.txt", "w")

with os.popen('arp -a') as f:
    data = f.read()

for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
    print(line)

#for mac in re.findall('([-0-9a-f]{17})\s+(\w+)',data):



file.write(data)



file.close()