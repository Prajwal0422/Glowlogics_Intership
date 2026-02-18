class Addition:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
        print("Sum:", self.a + self.b)

    def __del__(self):
        print("Memory cleared")

obj = Addition()
del obj