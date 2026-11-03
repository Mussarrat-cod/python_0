class Student:

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


class StudentManagement:

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            print("Student already exists!")
            return

        self.students[student.student_id] = student
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            student.display()
            print("----------------")

    def search_student(self, student_id):
        student = self.students.get(student_id)

        if student:
            student.display()
        else:
            print("Student not found.")

    def update_student(self, student_id, new_name, new_marks):
        student = self.students.get(student_id)

        if student:
            student.name = new_name
            student.marks = new_marks
            print("Student updated!")
        else:
            print("Student not found.")


def main():

    manager = StudentManagement()

    while True:
        print("\n1. Add student")
        print("2. Display students")
        print("3. Search student")
        print("4. Update student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_id = int(input("Student ID: "))
            name = input("Name: ")
            marks = float(input("Marks: "))

            student = Student(student_id, name, marks)
            manager.add_student(student)

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            student_id = int(input("Enter ID: "))
            manager.search_student(student_id)

        elif choice == "4":
            student_id = int(input("Enter ID: "))
            name = input("New name: ")
            marks = float(input("New marks: "))

            manager.update_student(student_id, name, marks)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()