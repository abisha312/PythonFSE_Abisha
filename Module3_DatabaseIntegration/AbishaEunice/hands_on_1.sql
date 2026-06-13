
-- Use Database
USE college_db;

-- 1. Departments Table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

-- 2. Students Table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,
    CONSTRAINT fk_students_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- 3. Courses Table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    CONSTRAINT fk_courses_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- 4. Enrollments Table
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    CONSTRAINT fk_enrollments_student
        FOREIGN KEY (student_id)
        REFERENCES students(student_id),
    CONSTRAINT fk_enrollments_course
        FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);

-- 5. Professors Table
CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    CONSTRAINT fk_professors_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- departments
INSERT INTO departments (dept_name, hod_name, budget) VALUES
  ('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
  ('Electronics', 'Dr. Priya Nair', 620000.00),
  ('Mechanical', 'Dr. Suresh Iyer', 540000.00),
  ('Civil', 'Dr. Ananya Sharma', 430000.00);
  
  -- students
INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, 
enrollment_year) VALUES
  ('Arjun',  'Mehta',    'arjun.mehta@college.edu',    '2003-04-12', 1, 2022),
  ('Priya',  'Suresh',   'priya.suresh@college.edu',   '2003-07-25', 1, 2022),
  ('Rohan',  'Verma',    'rohan.verma@college.edu',    '2002-11-08', 2, 2021),
  ('Sneha',  'Patel',    'sneha.patel@college.edu',    '2004-01-30', 3, 2023),
  ('Vikram', 'Das',      'vikram.das@college.edu',     '2003-09-14', 1, 2022),
  ('Kavya',  'Menon',    'kavya.menon@college.edu',    '2002-05-17', 2, 2021),
  ('Aditya', 'Singh',    'aditya.singh@college.edu',   '2004-03-22', 4, 2023),
  ('Deepika','Rao',      'deepika.rao@college.edu',    '2003-08-09', 1, 2022);
  
  -- courses
INSERT INTO courses (course_name, course_code, credits, department_id) VALUES
  ('Data Structures & Algorithms', 'CS101', 4, 1),
  ('Database Management Systems',  'CS102', 3, 1),
  ('Object Oriented Programming',  'CS103', 4, 1),
  ('Circuit Theory',               'EC101', 3, 2),
  ('Thermodynamics',               'ME101', 3, 3);
  
  -- enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
  (1, 1, '2022-07-01', 'A'), (1, 2, '2022-07-01', 'B'),
  (2, 1, '2022-07-01', 'B'), (2, 3, '2022-07-01', 'A'),
  (3, 4, '2021-07-01', 'A'), (4, 5, '2023-07-01', NULL),
  (5, 1, '2022-07-01', 'C'), (5, 2, '2022-07-01', 'A'),
  (6, 4, '2021-07-01', 'B'), (7, 5, '2023-07-01', NULL),
  (8, 1, '2022-07-01', 'A'), (8, 3, '2022-07-01', 'B');
  
-- professors
INSERT INTO professors (prof_name, email, department_id, salary) VALUES
  ('Dr. Anand Krishnan',  'anand.k@college.edu',   1, 95000.00),
  ('Dr. Meena Pillai',    'meena.p@college.edu',   1, 88000.00),
  ('Dr. Sunil Rajan',     'sunil.r@college.edu',   2, 82000.00),
  ('Dr. Latha Gopal',     'latha.g@college.edu',   3, 79000.00),
  ('Dr. Kartik Bose',     'kartik.b@college.edu',  4, 76000.00);
  

DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
DESCRIBE professors;

-- 1NF Analysis:
-- All columns contain atomic values.
-- No column stores multiple values in a single field.
-- Example violation: storing multiple phone numbers
-- like '9876543210,9876543211' in one column.

-- 2NF Analysis:
-- All tables use single-column primary keys.
-- In enrollments, attributes such as enrollment_date
-- and grade depend on the student-course enrollment.
-- No partial dependency exists.

-- 3NF Analysis:
-- No non-key attribute depends on another non-key attribute.
-- Department information is stored in departments table.
-- Storing dept_name inside students would create a
-- transitive dependency:
-- student_id -> department_id -> dept_name.
-- Therefore the schema satisfies 3NF.

-- Enrollments Table 3NF Analysis:
-- enrollment_id is the primary key.
-- student_id and course_id are foreign keys.
-- enrollment_date and grade depend directly on enrollment_id.
-- No non-key attribute determines another non-key attribute.
-- Therefore enrollments table satisfies 3NF.

-- Add phone_number Column
ALTER TABLE students
ADD COLUMN phone_number VARCHAR(15);

-- Add max_seats Column
ALTER TABLE courses
ADD COLUMN max_seats INT DEFAULT 60;

-- Add CHECK Constraint on Grade
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

-- Rename hod_name to head_of_dept
ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

-- Drop phone_number Column
ALTER TABLE students
DROP COLUMN phone_number;

-- verification
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;