'''
TASK 90 - N+1 QUERY COMPARISON

Before Optimization (N+1 Problem):
----------------------------------
Code:
    enrollments = session.query(Enrollment).all()

    for e in enrollments:
        print(e.student.first_name, "->", e.course.course_name)

Behavior:
    1 query retrieves all enrollment records.
    Additional queries are executed whenever
    e.student or e.course is accessed.

Query Count:
    1 query for enrollments
    N queries for students
    N queries for courses

    Total ≈ N+1 (or more)

Problem:
    As the number of enrollments increases,
    the number of SQL queries increases significantly,
    causing poor performance and excessive database
    round-trips.

After Optimization (joinedload):
--------------------------------
Code:
    enrollments = (
        session.query(Enrollment)
        .options(
            joinedload(Enrollment.student),
            joinedload(Enrollment.course)
        )
        .all()
    )

Behavior:
    SQLAlchemy performs JOINs and fetches
    enrollment, student, and course data
    in a single SQL statement.

Query Count:
    1 query total

Benefits:
    - Eliminates N+1 problem
    - Reduces database round-trips
    - Improves application performance
    - Scales efficiently for large datasets

Result:
    Both approaches return the same data,
    but joinedload reduces the query count
    from N+1 queries to 1 query.
'''

from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload

from models import (
    Department,
    Student,
    Course,
    Enrollment
)

engine = create_engine(
    "mysql+mysqlconnector://root:root@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# --------------------------------
# INSERT DEPARTMENTS
# --------------------------------

cs = Department(
    dept_name="Computer Science",
    hod_name="Dr Ramesh",
    budget=850000
)

ec = Department(
    dept_name="Electronics",
    hod_name="Dr Priya",
    budget=620000
)

me = Department(
    dept_name="Mechanical",
    hod_name="Dr Suresh",
    budget=540000
)

session.add_all([cs, ec, me])
session.commit()

# --------------------------------
# INSERT STUDENTS
# --------------------------------

s1 = Student(
    first_name="Arjun",
    last_name="Mehta",
    email="arjun@test.com",
    enrollment_year=2022,
    department=cs
)

s2 = Student(
    first_name="Priya",
    last_name="Suresh",
    email="priya@test.com",
    enrollment_year=2022,
    department=cs
)

s3 = Student(
    first_name="Rohan",
    last_name="Verma",
    email="rohan@test.com",
    enrollment_year=2021,
    department=ec
)

s4 = Student(
    first_name="Sneha",
    last_name="Patel",
    email="sneha@test.com",
    enrollment_year=2023,
    department=me
)

s5 = Student(
    first_name="Deepika",
    last_name="Rao",
    email="deepika@test.com",
    enrollment_year=2022,
    department=cs
)

session.add_all([s1, s2, s3, s4, s5])
session.commit()

# --------------------------------
# INSERT COURSES
# --------------------------------

c1 = Course(
    course_name="Data Structures",
    course_code="CS101",
    credits=4,
    department=cs
)

c2 = Course(
    course_name="DBMS",
    course_code="CS102",
    credits=3,
    department=cs
)

c3 = Course(
    course_name="Circuit Theory",
    course_code="EC101",
    credits=3,
    department=ec
)

session.add_all([c1, c2, c3])
session.commit()

# --------------------------------
# INSERT ENROLLMENTS
# --------------------------------

e1 = Enrollment(
    student=s1,
    course=c1,
    enrollment_date=date.today(),
    grade="A"
)

e2 = Enrollment(
    student=s2,
    course=c1,
    enrollment_date=date.today(),
    grade="B"
)

e3 = Enrollment(
    student=s3,
    course=c3,
    enrollment_date=date.today(),
    grade="A"
)

e4 = Enrollment(
    student=s5,
    course=c2,
    enrollment_date=date.today(),
    grade="A"
)

session.add_all([e1, e2, e3, e4])
session.commit()

# --------------------------------
# READ
# --------------------------------

students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name ==
        "Computer Science"
    )
)

print("\nComputer Science Students\n")

for s in students:
    print(s.first_name, s.last_name)

# --------------------------------
# N+1 QUERY
# --------------------------------

print("\nN+1 Example\n")

enrollments = session.query(Enrollment).all()

for e in enrollments:
    print(
        e.student.first_name,
        "->",
        e.course.course_name
    )

# --------------------------------
# FIX N+1
# --------------------------------

print("\nJoinedLoad Example\n")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        "->",
        e.course.course_name
    )

# --------------------------------
# UPDATE
# --------------------------------

student = (
    session.query(Student)
    .filter(
        Student.email ==
        "arjun@test.com"
    )
    .first()
)

student.enrollment_year = 2024
session.commit()

# --------------------------------
# DELETE
# --------------------------------

enrollment = (
    session.query(Enrollment)
    .first()
)

session.delete(enrollment)
session.commit()

print("\nCRUD completed successfully")