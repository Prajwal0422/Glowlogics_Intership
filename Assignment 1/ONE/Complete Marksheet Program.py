rno = int(input("Enter roll number: "))
name = input("Enter student name: ")

phy = int(input("Enter Physics marks: "))
mat = int(input("Enter Maths marks: "))
che = int(input("Enter Chemistry marks: "))

total = phy + mat + che
avg = total / 3

print("\n--- MARKSHEET ---")
print("Roll No:", rno)
print("Name:", name)
print("Physics:", phy)
print("Maths:", mat)
print("Chemistry:", che)
print("Total:", total)
print("Average:", avg)