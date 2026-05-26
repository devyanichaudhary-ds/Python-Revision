#Handle Division by Zero.
try:
    num1 =int(input("enter a number:"))
    num2 = int(input("enter a number:"))
    result = num1/num2
    print("Result:",result)

except ZeroDivisionError:
    print("cannot divide by zero")



#Handle Invalid Integer Input.
try:
    num=int(input("enter a number:"))
    print("You entered:",num)
except:
    print("Please enter a valid integer")



#Handle File Not Found Error
try:
    with open("data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("file does not exist ")



#Handle Multiple Exceptions
try:
    num = int(input("enter a number:"))
    result = 100/num
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")



#Use Finally Block
try:
    num = int(input("Enter number:"))
    print(10/num)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Program Finished")



#Create Custom Exception
class AgeError(Exception):
    pass
age=int(input("enter age:"))
try:
    if age<18:
        raise AgeError("Age must be 18 or above")
    print("Eligible")
except AgeError as e:
    print(e)



#Raise ValueError Manually
age = int(input("Enter age: "))

try:
    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Age:", age)

except ValueError as e:
    print(e)



#Safe Calculator Program
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("1. Add")
    print("2. Divide")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 / num2)

    else:
        print("Invalid Choice")

except ValueError:
    print("Enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")



#Handle Index Errors
numbers=[10,20,34]
try:
    index = int(input("Enter index:"))
    print(numbers[index])
except IndexError:
    print("Index out of range")

#ATM Withdrawal Validation
balance =20000
try:
    amount = int(input("enter withdrawal amount:"))
    if amount>balance:
        raise ValueError("Insufficient balance")
    balance -=amount
    print("withdrawal successful")
    print("remaining balance:",balance)
except ValueError as e:
    print(e)