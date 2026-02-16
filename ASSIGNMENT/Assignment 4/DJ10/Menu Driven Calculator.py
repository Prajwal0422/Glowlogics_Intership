def add():
    a=int(input())
    b=int(input())
    print(a+b)

def subtract():
    a=int(input())
    b=int(input())
    print(a-b)

def multiply():
    a=int(input())
    b=int(input())
    print(a*b)

def divide():
    a=int(input())
    b=int(input())
    print(a/b)

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

opt=int(input("Choose: "))

if opt==1:
    add()
elif opt==2:
    subtract()
elif opt==3:
    multiply()
elif opt==4:
    divide()
else:
    print("Invalid choice")