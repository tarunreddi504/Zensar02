
import sys
# print(sys.path)
sys.path.append("c:\Delhi")

for pth in sys.path:
    print(pth)

import gurgaon.mymodule as m

print("-" * 40)

m.greet(m.gname)
print(m.addMe(30, 40))
