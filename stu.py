students = {}

def add_student(name, marks):
    students[name] = marks

def display_students():
    for name, marks in students.items():
        print(name, marks)

def find_student(name):
    if name in students:
        print(students[name])
    else:
        print("Student not found")


add_student("A", 85)
add_student("B", 90)

display_students()
find_student("A")