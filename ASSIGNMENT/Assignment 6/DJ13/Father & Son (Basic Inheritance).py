class Father:

    def father_details(self):
        print("This is parent class")


class Son(Father):

    def son_details(self):
        print("This is derived class")


obj = Son()
obj.father_details()
obj.son_details()