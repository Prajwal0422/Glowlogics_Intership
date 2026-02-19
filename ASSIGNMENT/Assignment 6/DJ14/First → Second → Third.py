class First:
    def f1(self):
        print("This is First class")

class Second(First):
    def f2(self):
        print("This is Second class")

class Third(Second):
    def f3(self):
        print("This is Third class")

obj = Third()
obj.f3()
obj.f2()
obj.f1()