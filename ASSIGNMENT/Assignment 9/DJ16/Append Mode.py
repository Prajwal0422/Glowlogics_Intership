f1 = open("d:\\sample8.txt", "a")
f1.write("third line sample data\n")
f1.write("fourth line sample data\n")
f1.close()

f1 = open("d:\\sample8.txt", "r")
print(f1.read())
f1.close()