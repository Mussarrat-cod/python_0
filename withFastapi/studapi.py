from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

students = {}


@app.post("/students")
def create_student(student: dict):

    student_id = student["id"]

    if student_id in students:
        raise HTTPException(status_code=409, detail="Student already exists")

    students[student_id] = student

    return {"message": "Student created"}


@app.get("/students")
def get_students():
    return list(students.values())


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    del students[student_id]

    return {"message": "Student deleted"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)