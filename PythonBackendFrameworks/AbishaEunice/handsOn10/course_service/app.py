from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "course.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS course(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        code TEXT,
        credits INTEGER
    )
    """)

    conn.commit()
    conn.close()


create_table()


@app.route("/")
def home():
    return {"message": "Course Service Running"}


@app.route("/api/courses", methods=["POST"])
def create_course():

    data = request.json

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO course(name,code,credits)
        VALUES(?,?,?)
        """,
        (
            data["name"],
            data["code"],
            data["credits"]
        )
    )

    conn.commit()

    course_id = cursor.lastrowid

    conn.close()

    return jsonify(
        {
            "id": course_id,
            "message": "Course Created"
        }
    ), 201


@app.route("/api/courses", methods=["GET"])
def get_courses():

    conn = get_connection()

    courses = conn.execute(
        "SELECT * FROM course"
    ).fetchall()

    conn.close()

    return jsonify([dict(c) for c in courses])


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):

    conn = get_connection()

    course = conn.execute(
        "SELECT * FROM course WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if course is None:

        return jsonify(
            {
                "message": "Course Not Found"
            }
        ), 404

    return jsonify(dict(course))


if __name__ == "__main__":
    app.run(port=5001, debug=True)