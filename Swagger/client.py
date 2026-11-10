
import requests

BASE_URL = "http://127.0.0.1:5000"

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. View Student by ID")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student = {
            "id": int(input("Enter student ID: ")),
            "name": input("Enter name: "),
            "department": input("Enter department: "),
            "score": float(input("Enter score: "))
        }

        response = requests.post(
            f"{BASE_URL}/students",
            json=student
        )

        print(response.status_code, response.json())

    elif choice == "2":
        response = requests.get(f"{BASE_URL}/students")
        print(response.json())

    elif choice == "3":
        student_id = input("Enter student ID: ")

        response = requests.get(
            f"{BASE_URL}/students/{student_id}"
        )

        print(response.status_code, response.json())

    elif choice == "4":
        student_id = input("Enter student ID to delete: ")

        response = requests.delete(
            f"{BASE_URL}/students/{student_id}"
        )

        print(response.status_code, response.json())

    elif choice == "5":
        print("Exiting client...")
        break

    else:
        print("Invalid choice!")
