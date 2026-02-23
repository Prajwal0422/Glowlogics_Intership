with open("E:\\sample.txt", "r") as f2:
    data = f2.readlines()

for x in data:
    a1 = x.split()

print(a1)