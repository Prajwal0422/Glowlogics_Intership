class Calculate:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
        self.c = self.a + self.b

        print("A:", self.a)
        print("B:", self.b)
        print("Sum:", self.c)

obj = Calculate()