from flask import Flask, request, jsonify, send_file
from flask_swagger_ui import get_swaggerui_blueprint

from pathlib import Path
import yaml
import re


app = Flask(__name__)

students = {}

BASE_DIR = Path(__file__).resolve().parent
OPENAPI_FILE = BASE_DIR / "openapi.yaml"


def create_student():

    student = request.get_json()

    if not student or "id" not in student:
        return jsonify({"message": "Invalid student data"}), 400

    student_id = student["id"]

    if student_id in students:
        return jsonify({"message": "Student already exists"}), 409

    students[student_id] = student

    return jsonify({"message": "Student created"}), 201


def get_students():

    return jsonify(list(students.values()))


def get_student(student_id):

    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404

    return jsonify(students[student_id])


def delete_student(student_id):

    if student_id not in students:
        return jsonify({"message": "Student not found"}), 404

    del students[student_id]

    return jsonify({"message": "Student deleted"})


HANDLERS = {
    "createStudent": create_student,
    "getStudents": get_students,
    "getStudent": get_student,
    "deleteStudent": delete_student
}



def load_openapi():

    with open(OPENAPI_FILE, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)



def convert_path(path, parameters):

    parameter_types = {}

    for param in parameters:

        if param.get("in") == "path":

            parameter_types[param["name"]] = (
                param.get("schema", {}).get("type", "string")
            )

    def replace_parameter(match):

        name = match.group(1)

        param_type = parameter_types.get(name, "string")

        if param_type == "integer":
            return f"<int:{name}>"

        return f"<{name}>"

    return re.sub(r"\{([^}]+)\}", replace_parameter, path)



def register_routes():

    specification = load_openapi()

    for path, methods in specification["paths"].items():

        for method, details in methods.items():

            operation_id = details["operationId"]

            handler = HANDLERS.get(operation_id)

            if handler is None:
                raise ValueError(
                    f"No Python handler found for {operation_id}"
                )

            parameters = details.get("parameters", [])

            flask_path = convert_path(path, parameters)

            endpoint_name = f"{method}_{operation_id}"

            app.add_url_rule(
                flask_path,
                endpoint=endpoint_name,
                view_func=handler,
                methods=[method.upper()]
            )

            print(f"Registered: {method.upper()} {path}")


@app.route("/openapi.yaml")
def openapi_yaml():

    return send_file(OPENAPI_FILE)

swagger = get_swaggerui_blueprint(
    "/docs",
    "/openapi.yaml",
    config={"app_name": "Student API"}
)

app.register_blueprint(swagger)

if __name__ == "__main__":

    register_routes()
    app.run(debug=True, port=5000)