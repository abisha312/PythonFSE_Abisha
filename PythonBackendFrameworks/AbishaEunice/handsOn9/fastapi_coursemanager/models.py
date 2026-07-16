from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    head_of_dept = Column(String)
    budget = Column(Integer)

    courses = relationship("Course", back_populates="department")
    students = relationship("Student", back_populates="department")


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    enrollment_year = Column(Integer)
    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


class Enrollment(Base):
    __tablename__ = "enrollment"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    course_id = Column(Integer, ForeignKey("course.id"))
    enrollment_date = Column(Date)
    grade = Column(String)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Integer, default=1)