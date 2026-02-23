f1 = open("d:\\sample8.txt", "w")
f1.write("first line sample data\n")
f1.write("second line sample data\n")
f1.close()

f1 = open("d:\\sample8.txt", "r")
print(f1.read())
f1.close()