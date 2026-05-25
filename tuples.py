#Create and print tuple.
t=(1,2,3,4,5,6)
print(t)


#Find tuple length.
n=(12,34,21,44,26)
a = len(n)
print(a)


#Count occurrence of an element.
g = (12, 98, 67, 87, 67, 98)

occur = {}

for n in g:
    if n in occur:
        occur[n] += 1
    else:
        occur[n] = 1
print(occur)


#Find maximum element.
d=(12,36,19,27,17)
a=max(d)
print(a)


#Find minimum element.
a=(12,23,3,1,4,0,-1)
s=min(a)
print(s)


#Convert tuple to list.
e=(12,34,25,65)
f=list(e)
print(f)


#Convert list to tuple.
e=[12,45,34]
f=tuple(e)
print(f)


#Concatenate two tuples.
p=(18,98,67)
q=(78,65,45)
r= p+q
print("Concatenated tuple:",r)


#Find index of an element.
a=(34,87,56,78)
p=a.index(56)
print("the index is:",p)


#Unpack tuple values.
student = ("Devyani", 4, "Python")

name, day, course = student

print(name)
print(day)
print(course)