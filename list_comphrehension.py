#Create List of Squares.
squares=[x**2 for x in range(1,11)]
print(squares)


#Create List of Cubes
cubes=[x**3 for x in range(1,11)]
print(cubes)


#Filter Even Numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
even = [x for x in numbers if x%2==0]
print(even)


#Filter Odd Numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
odd= [x for x in numbers if x% 2!=0]
print(odd)


#Create List of Vowels from String.
text="education"
vowels=[ch for ch in text if ch.lower() in "aeiou"]
print(vowels)


#Convert Temperatures (Celsius → Fahrenheit)
celsius=[0,10,20,30,40]
fahrenheit=[(c*9/5)+32 for c in celsius]
print(fahrenheit)


#Create Multiplication Table List
table=[5*i for i in range(1,11) ]
print(table)


#Remove Negative Numbers.
numbers=[-5, 3, 4,-2]
positive=[x for x in numbers if x>=0]
print(positive)


#Flatten Nested List
nested = [[1,2],[3,4],[5,6]]
flat =[num for sublist in nested for num in sublist]
print(flat)


#Generate Prime Numbers
prime=[
    n for n in range(2,51)
    if all(n%i!=0 for i in range(2,n))
]
print(prime)