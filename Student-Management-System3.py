class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"\nRoll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")


students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = Student(roll, name, age, marks)
        students.append(student)

        print("Student Added Successfully!")

    # View Students
    elif choice == "2":
        if not students:
            print("No Students Found!")
        else:
            for student in students:
                student.display()

    # Search Student
    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        found = False

        for student in students:
            if student.roll_no == roll:
                student.display()
                found = True
                break

        if not found:
            print("Student Not Found!")

    # Update Student
    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")

        for student in students:
            if student.roll_no == roll:
                student.name = input("Enter New Name: ")
                student.age = int(input("Enter New Age: "))
                student.marks = float(input("Enter New Marks: "))

                print("Student Updated Successfully!")
                break
        else:
            print("Student Not Found!")

    # Delete Student
    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")

        for student in students:
            if student.roll_no == roll:
                students.remove(student)
                print("Student Deleted Successfully!")
                break
        else:
            print("Student Not Found!")

    # Exit
    elif choice == "6":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
import csv
with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, roll, age, marks])