s1 = (11,22,33,55,88)

x = int(input("Enter data: "))

if x in s1:
    print("Data found at index", s1.index(x))
else:
    print("Data not found")