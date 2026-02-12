a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a>b and a>c and a>d:
    print("Highest:", a)
elif b>a and b>c and b>d:
    print("Highest:", b)
elif c>a and c>b and c>d:
    print("Highest:", c)
else:
    print("Highest:", d)