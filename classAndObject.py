class myclass1():
    def myfunc(self,name):
        print("name is:", name)
    def display(self,name):
        print("Name is:",name)
MC = myclass1()
MC.myfunc('sridharblue')
MC.display('sridhar')

""" Instance and Static method"""

class sriclass():
    def instance(self):
        print("this is instance method")

    @staticmethod
    def static():
        print("this is static method")

mc=sriclass()
mc.instance()
mc.static()
sriclass.static()


""" class variables"""

class myclass2():
    a,b=100,200
    def add(self):
        print(myclass2.a+myclass2.b)
    def sub(self):
        print(self.b-self.a)
mc=myclass2()
mc.add()
mc.sub()


""" global, class, local varibles"""

a,b=100,200
class myclass():
    a,b=10,20
    def add(self, a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

mc=myclass()
mc.add(1000,2000)


