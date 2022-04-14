
import re

st = "The345345 quick brown fox jumps over the lazy dog"

res = re.search(r'\w+', st)

if res:
    print(res.group(0))
    print("Match found....")
else:
    print('Match not found......')