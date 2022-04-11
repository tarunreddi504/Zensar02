
def outerFun(gname):
    guest = f"Mr.{gname}"

    def innerFun():
        print(f"Hello {guest}")

    innerFun()

outerFun("Sachin")

