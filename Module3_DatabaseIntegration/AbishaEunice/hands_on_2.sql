INSERT INTO students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
VALUES
('Rahul', 'Sharma', 'rahul.sharma@college.edu', '2003-06-15', 1, 2022),
('Neha', 'Gupta', 'neha.gupta@college.edu', '2004-02-20', 2, 2023);

SELECT COUNT(*) AS total_students
FROM students;

UPDATE enrollments
SET grade = 'B'
WHERE student_id = 5
  AND course_id = 1;
  
SELECT *
FROM enrollments
WHERE student_id = 5
  AND course_id = 1;
  
SELECT *
FROM enrollments
WHERE grade IS NULL;

SET SQL_SAFE_UPDATES = 0; -- safe deletion cancellation
DELETE FROM enrollments
WHERE grade IS NULL;
SET SQL_SAFE_UPDATES = 1; -- safety mode on

SELECT COUNT(*) AS total_enrollments
FROM enrollments;

SELECT *
FROM students
WHERE enrollment_year = 2022
ORDER BY last_name ASC;

SELECT *
FROM courses
WHERE credits > 3
ORDER BY credits DESC;

SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;

SELECT *
FROM students
WHERE email LIKE '%@college.edu';

SELECT enrollment_year,
       COUNT(*) AS student_count
FROM students
GROUP BY enrollment_year
ORDER BY enrollment_year;

SELECT CONCAT(s.first_name, ' ', s.last_name) AS student_name,
       d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;

SELECT e.enrollment_id,
       CONCAT(s.first_name, ' ', s.last_name) AS student_name,
       c.course_name,
       e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;

SELECT s.student_id,
       CONCAT(s.first_name, ' ', s.last_name) AS student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

SELECT c.course_name,
       COUNT(e.student_id) AS enrolled_students
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT d.dept_name,
       p.prof_name,
       p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
ORDER BY d.dept_name;

SELECT c.course_name,
       COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT d.dept_name,
       ROUND(AVG(p.salary), 2) AS average_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name;

SELECT dept_name,
       budget
FROM departments
WHERE budget > 600000;

SELECT e.grade,
       COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade
ORDER BY e.grade;

SELECT d.dept_name,
       COUNT(s.student_id) AS student_count
FROM departments d
JOIN students s
ON d.department_id = s.department_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(s.student_id) > 2;