a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a<b and a<c and a<d:
    print("Smallest:", a)
elif b<a and b<c and b<d:
    print("Smallest:", b)
elif c<a and c<b and c<d:
    print("Smallest:", c)
else:
    print("Smallest:", d)
    