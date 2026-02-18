class Addition:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def add(self):
        print("Addition:", self.a + self.b)


class Subtraction:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def subtract(self):
        print("Subtraction:", self.a - self.b)


obj1 = Addition()
obj1.add()

obj2 = Subtraction()
obj2.subtract()