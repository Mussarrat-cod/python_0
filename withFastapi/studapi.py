from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {}


# Define student structure
class Student(BaseModel):
    id: int
    name: str
    department: str
    score: float


# POST - Create student
@app.post("/students")
def create_student(student: Student):

    student_id = student.id

    if student_id in students:
        raise HTTPException(
            status_code=409,
            detail="Student already exists"
        )

    students[student_id] = student.model_dump()

    return {"message": "Student created"}


# GET - Get all students
@app.get("/students")
def get_students():

    return list(students.values())


# DELETE - Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]

    return {"message": "Student deleted"}


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)