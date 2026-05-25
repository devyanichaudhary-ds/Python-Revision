#Print numbers from 1–100.
i=0
for i in range(1,101):
    i+=0
    print(i)


#Print multiplication table of a number.
a=int(input("enter a number:"))
i=1
for i in range(1,11):
    n=a*i
    print(f"{a}x{i}={n}")


#Sum first N natural numbers.
n=int(input("enter number:"))
total=0
for i in range(0,n+1):
    total+=i
print("sum =",total)


#Calculate factorial.
n=int(input('enter a number:'))
fact=1
for i in range(1,n+1):
    fact *=i
print("factorial :",fact)


#Print Fibonacci Series.
n=int(input('enter value of n:'))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#Count Digits in a Number.
n=int(input("enter a number:"))
count=0
while n>0:
    n = n//10
    count+=1
print("Digits =",count)


#Reverse a Number
n=int(input("enter a number:"))
reverse=0
while n>0:
    digit = n % 10
    reverse=reverse*10 + digit
    n = n // 10
print("reverse=",reverse)


#Check Armstrong Number
n =int(input('enter a number:'))
temp=n
total=0
while temp>0:
    digit = temp%10
    total+=digit **3
    temp //=10
if total ==n:
    print('armstrong number')
else:
    print("not armstrong number")


#Print Star Pyramid Pattern.
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


#Guess-the-Number Game.
import random 
guess =random.randint(1,20)
while True:
    num=int(input("enter a number:"))

    if num==guess:
        print("correct! you won!!")
        break
    elif num<guess:
        print("too low.")
    elif num>guess:
        print("too high.")
    else:
        print("play again!")