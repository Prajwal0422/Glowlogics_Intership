class Calculate:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def add(self):
        print("Add:", self.a + self.b)

    def subtract(self):
        print("Subtract:", self.a - self.b)

obj = Calculate()
obj.add()
obj.subtract()
