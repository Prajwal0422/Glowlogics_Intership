city = input("Enter city: ")
age = int(input("Enter age: "))
exp = int(input("Enter experience: "))

if city == "bangalore" and age <= 30 and exp >= 5:
    print("Selected")
else:
    print("Not selected")