#Take name and age as input and print a greeting.
name = input("enter name:")
age=int(input("enter age:"))
print(f"Hello {name} , your age is {age}.")

#Input two numbers and print their sum, difference, product, and quotient.

a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
sum = a+b
difference= a-b
product = a*b
quotient =  a/b
print("the sum of two number is:",sum)
print("the difference of two number is:", difference)
print("the product of two number is:",product)
print("the quoitient of two number is:",quotient)

#Convert Celsius to Fahrenheit.
C=int(input("enter temprature in celsius:"))
F=(C*9/5)+32
print(f"temprature in farhrenheit is:{F}°f")

#Find area of a rectangle.
l=int(input("enter length:"))
b=int(input("enter breadth:"))
area=l*b
print("the area of rectangle is:",area)

#Swap two numbers without using a third variable.
a=int(input("Enter value of a:"))
b=int(input("Enter value of b :"))
a,b=b,a
print("a =", a)
print("b =", b)

#Calculate simple interest.
P=int(input("enter principal:"))
R=int(input("enter rate of interest:"))
T=int(input("enter time:"))
SI=P*R*T
print("the simple interest is:",SI)

#Find square and cube of a number.
a = int(input("Enter value of a:"))
square=a*a
cube=a*a*a
print(f"the square of {a} is {square}")
print(f"the cube of {a} is {cube}")

#Convert minutes into hours and minutes.
total_minutes = int(input("Enter minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print("Hours:", hours)
print("Minutes:", minutes)

#Calculate percentage from 5 subject marks.
sub1=int(input("enter marks of sub1:"))
sub2=int(input("enter marks of sub2:"))
sub3=int(input("enter marks of sub3:"))
sub4=int(input("enter marks of sub4:"))
sub5=int(input("enter marks of sub5:"))
total = sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
print(f"the percentage of 5 subjects is {percentage}%")

#Find the largest among three numbers.
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
if a>b and a>c:
    print("a is largest.")
elif b>a and b>c:
    print("b is largest.")
elif c>a and c>b:
    print("c is largest.")
elif a==b and c==b and a==c:
    print("none is largest.")
else:
    print("try again!!")

