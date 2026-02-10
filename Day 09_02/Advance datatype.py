x1=[11,22,33,44,55]
a1=["ram","steven"]
a1.extend(x1)
print(x1)
print(a1)
for i in x1:
    print(x1)

f1.append(a1)
print(f1)
s1=['aa','bb','cc']
s1.remove('aa')
print(s1)

q1=[11,22,33,44,55]
q1.pop(2)
print(q1)

#slicing
d1=['qq',11,22,33]
print(d1)
d2=d1[2:]
print(d2)

d3=d1[::-1]
print(d3)

#len
print(len(d2))

#count : counts how many times the value is in the variable
print(d2.count(11))

#deleting all the data
s1.clear()
print(s1) # gives empty list
del s1 # error
