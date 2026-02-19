class Subtract(Addition):

    def subtract(self):
        print("Subtraction:", self.a - self.b)


obj = Subtract()
obj.add()        # inherited method
obj.subtract()   # own method