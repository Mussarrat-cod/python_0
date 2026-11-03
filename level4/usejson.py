import json

students = [
    {
        "id": 1,
        "name": "Rahul",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Priya",
        "marks": 92
    }
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for student in data:
    print(student["name"], student["marks"])