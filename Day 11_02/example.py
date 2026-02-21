class Addition:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print("Addition:", self.a+self.b)

class Subtraction:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print("Subtraction:", self.a-self.b)

class Multiply:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print("Multiply:", self.a*self.b)

class Divide:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print("Divide:", self.a/self.b)


Addition().calc()
Subtraction().calc()
Multiply().calc()
Divide().calc()