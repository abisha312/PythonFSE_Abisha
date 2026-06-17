import mysql.connector
import time

# Update these values according to your MySQL setup
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "college_db"
}


def n_plus_one_demo():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    query_count = 0

    start_time = time.time()

    # Query 1: Get all enrollments
    cursor.execute("SELECT * FROM enrollments")
    enrollments = cursor.fetchall()
    query_count += 1

    results = []

    # N additional queries
    for enrollment in enrollments:
        cursor.execute(
            """
            SELECT first_name, last_name
            FROM students
            WHERE student_id = %s
            """,
            (enrollment["student_id"],)
        )

        student = cursor.fetchone()
        query_count += 1

        results.append({
            "enrollment_id": enrollment["enrollment_id"],
            "student_name": f"{student['first_name']} {student['last_name']}",
            "course_id": enrollment["course_id"],
            "grade": enrollment["grade"]
        })

    end_time = time.time()

    print("\n===== N+1 QUERY APPROACH =====")
    print(f"Queries Executed: {query_count}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    print(f"Rows Retrieved: {len(results)}")

    conn.close()


def join_demo():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    start_time = time.time()

    cursor.execute("""
        SELECT
            e.enrollment_id,
            s.first_name,
            s.last_name,
            e.course_id,
            e.grade
        FROM enrollments e
        JOIN students s
            ON e.student_id = s.student_id
    """)

    results = cursor.fetchall()

    end_time = time.time()

    print("\n===== SINGLE JOIN APPROACH =====")
    print("Queries Executed: 1")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    print(f"Rows Retrieved: {len(results)}")

    conn.close()


if __name__ == "__main__":
    print("N+1 Problem Demonstration")
    print("-" * 40)

    n_plus_one_demo()
    join_demo()

'''
N+1 Problem Demonstration
----------------------------------------
===== N+1 QUERY APPROACH =====
Queries Executed: 13
Execution Time: 0.008126 seconds
Rows Retrieved: 12

===== SINGLE JOIN APPROACH =====
Queries Executed: 1
Execution Time: 0.000000 seconds
Rows Retrieved: 12

Comparison:
N+1 Approach = 1 query + N additional queries
JOIN Approach = 1 query total
For 10,000 enrollments:
N+1 -> 10,001 queries
JOIN -> 1 query
'''