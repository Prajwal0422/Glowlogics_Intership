s1={1:'aaa',2:'bbb',3:'ccc',4:'ddd'}
print(s1)
s1.clear()
print(s1)

s1={1:'aaa',2:'bbb'}
del s1 #command
# print(s1)

s1={1:'aaa',2:'bbb'}
x=print(s1.get(2))
print(s1[1])

print(x)

print(s1.items())
print(s1.values())
print(s1.keys())

y=(s1.values())
print(y)

t1={1:'aaa',2:'bbb',3:'ccc',4:'ddd'}
print(t1)

t2={1:'aaa',2:'bbb',3:'ccc',4:'ddd'}
print(t2)

t3=t1.update(t2)
print(t3)
print(t1.update(t2))
print(t1)

j1={1,2,3,4,5}
print(j1)

j1.discard(3)
print(j1)
j1.pop()
print(j1)