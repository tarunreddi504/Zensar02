
import re

def regEx(ln1):
    res = re.search(r'[0-9][0-9][0-9][1-9]',ln1)
    if res:
        print(res.group(0))
        print("Match found")
    else:
        print("Match not found")

regEx("0000")
regEx("0001")
regEx("10000")