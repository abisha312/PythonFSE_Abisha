from fastapi import FastAPI, HTTPException, Depends, status, BackgroundTasks
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from database import get_db
from models import Course, Student, Enrollment
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
)

app = FastAPI(

    title="Course Management API",

    description="Backend API for managing departments, courses, students and enrollments.",

    version="1.0",

    contact={
        "name":"Abisha Eunice",

        "email":"admin@college.edu"
    }

)


@app.get("/")
async def root():
    return {"message":"API running"}


@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):

    new_course = Course(**course.model_dump())

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    return new_course

@app.get(
    "/api/courses/{id}",
    response_model=CourseResponse
)
async def get_course(
    id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    course = result.scalar_one_or_none()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course

@app.get("/api/courses/{id}/students/")
async def course_students(
    id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student)
        .join(Enrollment)
        .where(Enrollment.course_id == id)
    )

    students = result.scalars().all()

    return students

@app.get(
    "/api/courses/",
    response_model=list[CourseResponse],
    tags=["Courses"]
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):

    query = select(Course)

    if department_id is not None:
        query = query.where(
            Course.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()



@app.get("/api/students/")
async def get_students(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(select(Student))

    return result.scalars().all()

@app.post("/api/students/")
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):

    obj = Student(**student.model_dump())

    db.add(obj)

    await db.commit()

    await db.refresh(obj)

    return obj

@app.get("/test")
async def test(
    db:AsyncSession=Depends(get_db)
):

    return {
        "message":"Database Connected"
    }

@app.put(
    "/api/courses/{id}",
    response_model=CourseResponse
)
async def update_course(
    id: int,
    updated_course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    course = result.scalar_one_or_none()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    data = updated_course.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(course, key, value)

    await db.commit()

    await db.refresh(course)

    return course

@app.delete(
    "/api/courses/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(
    id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    course = result.scalar_one_or_none()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)

    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)



def send_confirmation_email(email: str):

    print(f"Sending confirmation to {email}")

@app.post("/api/enrollments/")
async def create_enrollment(

    enrollment: EnrollmentCreate,

    background_tasks: BackgroundTasks,

    db: AsyncSession = Depends(get_db)

):

    obj = Enrollment(**enrollment.model_dump())

    db.add(obj)

    await db.commit()

    await db.refresh(obj)

    student = await db.get(Student, obj.student_id)

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return obj