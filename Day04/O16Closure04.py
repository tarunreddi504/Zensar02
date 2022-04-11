
def outerFun(greet):                # Higher order Function (HOF)

    def innerFun(sep):

        def innerMostFun(name):
            from emojis import emojis
            emojised = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojised)

        return innerMostFun

    return innerFun


engGrt = outerFun("Welcome")
tgrEmj = engGrt("tiger")
tgrEmj("Sheroff")

hndGrt = outerFun("Namaskar")
elpntEmj = hndGrt("elephant")
elpntEmj("Amjad Khan")



"""
print("-" * 40)
outerFun("Welcome")("=====>")("Sachin")

print("-" * 40)
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")

print("-" * 40)
sngLn = engGrt("----->")
dbln = hndGrt("=====>>")
strln = tmlGrt("******>>")

print("-" * 40)
sngLn("Sunil Gavaskar")
dbln("Kapil Dev")
strln("Kris Srikanth")
"""