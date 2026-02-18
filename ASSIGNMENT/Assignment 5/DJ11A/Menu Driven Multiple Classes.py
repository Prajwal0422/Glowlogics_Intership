class Addition:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print(self.a+self.b)

class Subtraction:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print(self.a-self.b)

class Multiply:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print(self.a*self.b)

class Divide:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
    def calc(self):
        print(self.a/self.b)


print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

opt = int(input("Choose option: "))

if opt==1:
    Addition().calc()
elif opt==2:
    Subtraction().calc()
elif opt==3:
    Multiply().calc()
elif opt==4:
    Divide().calc()
else:
    print("Invalid choice")
