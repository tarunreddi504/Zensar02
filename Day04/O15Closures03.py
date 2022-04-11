
def outerFun(greet):

    def innerFun(name):

        print(greet, name)

    return innerFun

outerFun("Hello")("Sachin")

hindiGrt = outerFun("Namaskar")
tamilGrt = outerFun("Vanakam")
spanisGrt = outerFun("Hola")

# simple curry

hindiGrt("Jadeja")
tamilGrt("Natraj")
spanisGrt("Messi")
