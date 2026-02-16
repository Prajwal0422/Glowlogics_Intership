def student():
    rno=int(input("Roll No: "))
    name=input("Name: ")
    phy=int(input("Physics: "))
    mat=int(input("Maths: "))
    che=int(input("Chemistry: "))

    total=phy+mat+che
    avg=total/3

    print("Total:", total)
    print("Average:", avg)

student()