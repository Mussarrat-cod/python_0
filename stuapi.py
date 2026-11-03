from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

stance = FastAPI()

students = {}


class Student(BaseModel):
    id: int
    name: str
    department: str
    score: float
    


@stance.post("/students")
def create_student(student: Student):

    if student.id in students:
        raise HTTPException(
            status_code=409,
            detail="Student already exists"
        )

    students[student.id] = student

    return {"message": "Student created"}


@stance.get("/students")
def get_students():
    return list(students.values())


@stance.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    return students[student_id]


@stance.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    del students[student_id]

    return {"message": "student deleted"}