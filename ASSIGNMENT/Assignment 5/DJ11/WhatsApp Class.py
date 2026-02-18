class WhatsApp:

    def __init__(self):
        self.name = input("Enter name: ")
        self.ph = input("Enter phone: ")
        self.msg = input("Enter message: ")

    def send(self):
        print("Sending message...")
        print(self.name, self.ph, self.msg)

obj2 = WhatsApp()
obj2.send()