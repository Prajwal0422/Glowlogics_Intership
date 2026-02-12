s1 = (11,22,33,55,88)

x = int(input("Enter data: "))

for i in s1:
    if x == i:
        print("Data found")
        break
else:
    print("Data not found")