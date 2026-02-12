marks = int(input("Enter marks: "))

if marks > 85:
    print("Grade A")
elif marks > 60:
    print("Grade B+")
elif marks > 40:
    print("Grade B")
elif marks > 30:
    print("Grade C")
else:
    print("Fail")