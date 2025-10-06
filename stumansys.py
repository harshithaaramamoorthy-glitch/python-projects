class Student:
    def _init_(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def accept(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        student = Student(roll_no, name, age, grade)
        self.students.append(student)
        print("Student added successfully!")

    def display(self):
        if not self.students:
            print("No students in the database.")
        else:
            for i, student in enumerate(self.students, start=1):
                print(f"Student {i}:")
                print(f"Roll No: {student.roll_no}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
                print("-------------------------")

    def search(self):
        roll_no = input("Enter Roll No to search: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Roll No: {student.roll_no}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
                return
                print("Student not found.")

    def delete(self):
        roll_no = input("Enter Roll No to delete: ")
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
                print("Student not found.")

    def update(self):
        roll_no = input("Enter Roll No to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = input("Enter new Name: ")
                student.age = input("Enter new Age: ")
                student.grade = input("Enter new Grade: ")
                print("Student updated successfully!")
                return
                print("Student not found.")

def main():
    sms = StudentManagementSystem()
    while True:
        print("Student Management System")
        print("1. Accept")
        print("2. Display")
        print("3. Search")
        print("4. Delete")