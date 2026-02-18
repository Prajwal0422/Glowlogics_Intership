class Highest:

    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

        if self.a > self.b:
            print("First number is highest")
        else:
            print("Second number is highest")

obj = Highest()