class Addition:
    def __init__(self):
        self.a = int(input("Enter first number for addition: "))
        self.b = int(input("Enter second number for addition: "))
        self.z = self.a + self.b
        print("Addition:", self.z)

class Subtraction(Addition):
    def __init__(self):
        super().__init__()  # calls Addition constructor
        self.x = int(input("Enter first number for subtraction: "))
        self.y = int(input("Enter second number for subtraction: "))
        self.z1 = self.x - self.y
        print("Subtraction:", self.z1)

class Multiply(Subtraction):
    def __init__(self):
        super().__init__()  # calls Subtraction constructor
        self.p = int(input("Enter first number for multiplication: "))
        self.q = int(input("Enter second number for multiplication: "))
        self.z2 = self.p * self.q
        print("Multiplication:", self.z2)

obj = Multiply()