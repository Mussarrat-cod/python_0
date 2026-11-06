
from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}


@app.route("/students", methods=["POST"])
def create_student():

    student = request.get_json()

    student_id = student["id"]

    if student_id in students:
        return jsonify({"message": "Student already exists"}), 409

    students[student_id] = student

    return jsonify({"message": "Student created"}), 201


@app.route("/students", methods=["GET"])
def get_students():

    return jsonify(list(students.values()))


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404

    return jsonify(students[student_id])


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404

    del students[student_id]

    return jsonify({"message": "Student deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
