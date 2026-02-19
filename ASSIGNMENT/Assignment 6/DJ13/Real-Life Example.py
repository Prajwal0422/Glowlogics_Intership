class Father:

    def details(self):
        print("Works in Wipro")
        print("Age: 50")
        print("Stays in Jayanagar")


class Son(Father):

    def info(self):
        print("Studies in CMR College")
        print("Age: 23")


obj = Son()
obj.details()   # inherited
obj.info()