from fastapi import FastAPI, HTTPException, Depends, status, BackgroundTasks
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,or_
from typing import Optional
from models import Base
from database import get_db, engine
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

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message":"API running"}


@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_course(
    response: Response,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):

    new_course = Course(**course.model_dump())

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    response.headers["Location"] = f"/api/courses/{new_course.id}/"

    return new_course


@app.get(
    "/api/v1/courses/{id}",
    response_model=CourseResponse,
    tags=['Courses']
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

@app.get("/api/v1/courses/{id}/students/", tags=['Courses'])
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


@app.get("/api/v1/courses/", tags=['Courses'])
async def get_courses(
    page: int = 1,
    page_size: int = 2,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):

    offset = (page - 1) * page_size

    query = select(Course)

    if search:
        query = query.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%")
            )
        )

    total = (await db.execute(query)).scalars().all()
    count = len(total)

    query = query.offset(offset).limit(page_size)

    result = await db.execute(query)

    courses = result.scalars().all()

    next_page = None
    previous_page = None

    if offset + page_size < count:
        next_page = f"/api/v1/courses/?page={page+1}&page_size={page_size}"

    if page > 1:
        previous_page = f"/api/v1/courses/?page={page-1}&page_size={page_size}"

    return {
        "count": count,
        "next": next_page,
        "previous": previous_page,
        "results": courses
    }



@app.get("/api/v1/students/", tags=['Students'])
async def get_students(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(select(Student))

    return result.scalars().all()

@app.post("/api/v1/students/", tags=['Students'])
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
    "/api/v1/courses/{id}",
    response_model=CourseResponse,
    tags=['Courses']
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

@app.patch(
    "/api/courses/{id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def patch_course(
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

    update_data = updated_course.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)

    return course

@app.delete(
    "/api/v1/courses/{id}",
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

@app.post("/api/v1/enrollments/")
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