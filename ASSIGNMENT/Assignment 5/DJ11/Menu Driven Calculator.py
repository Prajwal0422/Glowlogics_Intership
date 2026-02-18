class Calculate:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def add(self):
        print(self.a+self.b)

    def subtract(self):
        print(self.a-self.b)

    def multiply(self):
        print(self.a*self.b)

    def divide(self):
        print(self.a/self.b)

obj = Calculate()

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

opt = int(input("Choose option: "))

if opt==1:
    obj.add()
elif opt==2:
    obj.subtract()
elif opt==3:
    obj.multiply()
elif opt==4:
    obj.divide()
else:
    print("Invalid choice")