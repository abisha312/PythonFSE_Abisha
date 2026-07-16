from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

DATABASE = "student.db"

COURSE_SERVICE = "http://localhost:5001"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():

    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS enrollment(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER
    )
    """)

    conn.commit()

    conn.close()


create_tables()


@app.route("/")
def home():

    return {
        "message": "Student Service Running"
    }


@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.json

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO student(name,email)
        VALUES(?,?)
        """,
        (
            data["name"],
            data["email"]
        )
    )

    conn.commit()

    student_id = cursor.lastrowid

    conn.close()

    return jsonify(
        {
            "id": student_id,
            "message": "Student Created"
        }
    ), 201


@app.route("/api/students", methods=["GET"])
def get_students():

    conn = get_connection()

    students = conn.execute(
        "SELECT * FROM student"
    ).fetchall()

    conn.close()

    return jsonify([dict(s) for s in students])


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll_student(id):

    data = request.json

    course_id = data["course_id"]

    try:

        response = requests.get(
            f"{COURSE_SERVICE}/api/courses/{course_id}"
        )

    except requests.exceptions.ConnectionError:

        return jsonify(
            {
                "message": "Course Service Unavailable"
            }
        ), 503

    if response.status_code != 200:

        return jsonify(
            {
                "message": "Course Not Found"
            }
        ), 404

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO enrollment(student_id,course_id)
        VALUES(?,?)
        """,
        (
            id,
            course_id
        )
    )

    conn.commit()

    conn.close()

    return jsonify(
        {
            "message": "Enrollment Successful"
        }
    ), 201


if __name__ == "__main__":
    app.run(port=5002, debug=True)