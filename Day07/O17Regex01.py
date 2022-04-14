"""
functions in re library
-----------------------
1. match
2. search
3. findall
4. finditer
5. compile
6. sub
7. fullmatch


"""
import re

# st = "hello world"
# res = re.match(r'^hello', st)
# res = re.search(r'world$', st)
# res = re.search(r'b..t', st)
# res = re.search(r'ba*t', st)
# res = re.search(r'ba?t', st)
# res = re.search(r'ba+t', st)
# res = re.search(r'ba{3}t', st)
# res = re.search(r'ba{3,}t', st)
# res = re.search(r'ba{3,8}t', st)
# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[^aeiou]t', st)
# res = re.search(r'b(oa|ai)t', st)


st = "sample.py"

res = re.search(r'\.py$', st)

if res:
    # print(res)
    print(res.group(0))                     # string that matched our regular expression
    print("Match found....")
else:
    print('Match not found......')