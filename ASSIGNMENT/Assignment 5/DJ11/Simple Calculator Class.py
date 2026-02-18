class Calculate:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
        self.c = 0

    def add(self):
        self.c = self.a + self.b
        print("Addition:", self.c)

obj = Calculate()
obj.add()