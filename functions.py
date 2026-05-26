#Function to add two numbers.
def add(a,b):
    return a + b
result=add(78,65)
print("Sum =",result)


#Function to Find Maximum
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(23,45))


#Function to Check Prime Number
def prime(a):
    if a<=1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
num =int(input("enter a number: "))
if prime(num):
    print("Prime")
else:
    print("Not prime")


#Function to Calculate Factorial.
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact*= i
    return fact
print(factorial(5))


#Recursive Factorial Function
def factorial(n):
    if n ==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))


#Recursive Fibonacci Function
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(7):
    print(fibonacci(i), end=" ")


#Lambda Function for Square.
square = lambda x: x *x
print(square(5))


#Lambda Function for Sorting
students = [
    ("Riya",90),
    ("Ananya",79),
    ("Diya",56)
]
students.sort(key=lambda x: x[0])
print(students)


#Function to Count Vowels
def count_vowels(text):
    count=0
    for ch in text.lower():
        if ch in "aeiou":
            count +=1

    return count
print(count_vowels("english"))


#Calculator Using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Choose (+, -, *, /): ")

if choice == "+":
    print(add(num1, num2))

elif choice == "-":
    print(subtract(num1, num2))

elif choice == "*":
    print(multiply(num1, num2))

elif choice == "/":
    print(divide(num1, num2))

else:
    print("Invalid choice")