class GrandFather:
    def f1(self):
        print("This is Grandfather class")

class Father(GrandFather):
    def f2(self):
        print("This is Father class")

class Son(Father):
    def f3(self):
        print("This is Son class")

obj = Son()
obj.f1()
obj.f2()
obj.f3()