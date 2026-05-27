#Create Student Class
class Student:
    def __init__(self,name, marks):
        self.name =name
        self.marks = marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
s1 = Student("Devyani",98)
s1.display()


#Create Rectangle Class and Area Method
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
r1 =Rectangle(10,3)
print("Area=",r1.area())


#Create Employee Class
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Salary:", self.salary)
e1=Employee("Ashna",50000)
e1.display()


#Create BankAccount Class
class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance =", self.balance)


account = BankAccount()

account.deposit(1000)
account.withdraw(200)
account.check_balance()


#Create Car Class with Constructor
class Car:
    def __init__(self,brand,model):
        self.brand =  brand
        self.model = model
    def display(self):
        print(self.brand,self.model)
c1 =Car("Maruti Suzuki","Maruti 800")
c1.display()


#Single Inheritance Example
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    pass
d = Dog()
d.sound()


#Multilevel Inheritance Example
class Grandparent:
    def house(self):
        print("Owns a house")
class Parent(Grandparent):
    def car(self):
        print("Owns a car")
class child(Parent):
    pass
c=child()
c.house()
c.car()


#Method Overriding Example.
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()


#Library Management System
class Library:

    def __init__(self):
        self.books = ["Python", "Java", "C++"]

    def show_books(self):
        print(self.books)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book borrowed")
        else:
            print("Book unavailable")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned")


lib = Library()

lib.show_books()

lib.borrow_book("Python")

lib.show_books()



#Student Management System
class StudentManagement:

    def __init__(self):
        self.students = {}

    def add_student(self, roll, name):
        self.students[roll] = name

    def display(self):
        print(self.students)


sms = StudentManagement()

sms.add_student(101, "Devyani")
sms.add_student(102, "Riya")

sms.display()