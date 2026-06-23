class myClass:
    __privateVar = 27;
def __privMeth(self):
    print("i am inside class myclass")
def hello(self):
    print("private variable value:", myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privMeth