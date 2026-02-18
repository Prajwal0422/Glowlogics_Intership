class Contacts:

    def __init__(self):
        self.name = input("Enter name: ")
        self.ph = input("Enter phone: ")

    def save(self):
        print("Name:", self.name)
        print("Phone:", self.ph)

obj1 = Contacts()
obj1.save()