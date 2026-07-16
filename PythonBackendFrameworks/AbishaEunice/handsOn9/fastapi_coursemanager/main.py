from fastapi import FastAPI, HTTPException, Depends, status, BackgroundTasks
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,or_
from typing import Optional
from models import Base
from database import get_db, engine
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from models import Course, Student, Enrollment, User
from jose import JWTError, jwt
from security import SECRET_KEY, ALGORITHM, get_password_hash, verify_password, create_access_token
from fastapi.middleware.cors import CORSMiddleware
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
    UserRegister, 
    UserLogin, 
    Token
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# OAuth2 Authorization Code Flow:
# User is redirected to an authorization server,
# grants permission,
# receives an authorization code,
# which is exchanged for an access token.
#
# Our implementation is simpler:
# User directly sends email and password,
# and receives a JWT token immediately.
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/"
)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    result = await db.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    return user

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
    current_user: User = Depends(get_current_user),
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
    current_user: User = Depends(get_current_user),
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


@app.post("/api/v1/auth/register/")
async def register_user(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.email == user.email)
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )
    hashed = get_password_hash(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {
        "message": "User Registered Successfully"
    }



@app.post(
    "/api/v1/auth/login/",
    response_model=Token
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )

    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
   