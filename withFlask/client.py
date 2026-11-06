
import requests

url = "http://127.0.0.1:5000/students"

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_id = int(input("Enter ID: "))
        name = input("Enter name: ")
        department = input("Enter department: ")
        score = float(input("Enter score: "))

        student = {
            "id": student_id,
            "name": name,
            "department": department,
            "score": score
        }

        response = requests.post(url, json=student)
        print(response.json())

    elif choice == "2":
        response = requests.get(url)
        print("\nAll Students:")
        print(response.json())

    elif choice == "3":
        student_id = int(input("Enter ID to delete: "))

        response = requests.delete(
            f"{url}/{student_id}"
        )
        print(response.json())

    elif choice == "4":
        break
