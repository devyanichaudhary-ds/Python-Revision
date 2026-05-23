#Check if a number is positive or negative.
a=int(input("enter a number:"))
if a>0:
    print("its a positive number.")
elif a<0:
    print("its a negative number.")
else:
    print("its a zero.")

#Check if a number is even or odd.
n=int(input("enter a number:"))
if n%2==0:
    print("its a even number.")
else:
    print("its a odd number.")

#Find largest among three numbers.
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>b and a>c:
    print("a is largest.")
elif b>a and b>c:
    print("b is largest.")
elif c>a and c>b:
    print("c is largest.")
elif a==b or b==c or a==c:
    print("none is largest.")
else:
    print("try again!!")

#Check voting eligibility.
age=int(input("enter age:"))
if age>18:
    print("you can vote!")
elif age==18:
    print("you can vote!")
elif age<18:
    print("you can't vote.")
else:
    print("enter appropriate age.")

#Grade calculator based on marks.
maths=int(input("enter your maths marks:"))
science=int(input("enter your science marks:"))
english=int(input("enter your english marks:"))
total= ((maths+science+english)/300)*100
print("total is:",total)
if total>=90:
    print("your grade is A")
elif total>=80:
    print("your grade is B.")
elif total>=70:
    print("your grade is C.")
elif total>=60:
    print("your grade is D.")
elif total>=50:
    print("your grade is E.")
else:
    print("Better luck Next time.")

#Check leap year.
year = int(input("enter year:"))
if (year %4==0 and year %100 != 0) or (year%400==0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year.")

#Calculate electricity bill using slabs.
units = float(input("Enter units consumed: "))

if units <= 100:
    bill = units * 3
else:
    bill = (100 * 3) + ((units - 100) * 5)

print(f"Total Bill: ₹{bill}")

#Determine triangle type.
a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))
if a == b == c:
    print("Equilateral Triangle (All sides equal)")
elif a == b or b == c or a == c:
    print("Isosceles Triangle (Two sides equal)")
else:
    print("Scalene Triangle (All sides different)")

#Check whether a character is vowel or consonant.
ch=input("enter a character:")
if ch in ('a', 'e', 'i', 'o', 'u'):
    print("its a vowel.")
else:
    print("its a consonent.")

#Create a simple login system.
name = input("enter your FULL NAME:")
age=int(input("enter your AGE:"))
password =input("enter Password:")
if name=='sabrina' and age==34 and password=='espresso':
    print("Login Successfully.")
else:
    print("try again!")
