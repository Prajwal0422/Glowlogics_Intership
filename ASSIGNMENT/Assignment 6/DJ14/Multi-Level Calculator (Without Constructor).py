class Addition:
    def add(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Addition:", a+b)

class Subtraction(Addition):
    def subtract(self):
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Subtraction:", x-y)

class Multiply(Subtraction):
    def multiply(self):
        p = int(input("Enter first number: "))
        q = int(input("Enter second number: "))
        print("Multiplication:", p*q)

obj = Multiply()
obj.add()
obj.subtract()
obj.multiply()