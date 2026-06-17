USE college_db;

EXPLAIN FORMAT=JSON
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- ouput ({"query": "/* select#1 */ select `s`.`first_name` AS `first_name`,`s`.`last_name` AS `last_name`,`c`.`course_name` AS `course_name` from `college_db`.`enrollments` `e` join `college_db`.`students` `s` join `college_db`.`courses` `c` where ((`e`.`stude...)

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);



SELECT student_id,
       course_id,
       COUNT(*)
FROM enrollments
GROUP BY student_id, course_id
HAVING COUNT(*) > 1;

CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id, course_id);

-- removing duplicates
SELECT *
FROM enrollments
WHERE student_id = 1
  AND course_id = 5;
  
DELETE FROM enrollments
WHERE enrollment_id = 15;

-- testing duplicate prevention
INSERT INTO enrollments
(student_id, course_id, enrollment_date, grade)
VALUES
(1,1,CURDATE(),'A');



CREATE INDEX idx_course_code
ON courses(course_code);

-- on rerun of explain (EXPLAIN { "query": "/* select#1 */ select `s`.`first_name` AS `first_name`,`s`.`last_name` AS `last_name`,`c`.`course_name` AS `course_name` from `college_db`.`enrollments` `e` join `college_db`.`students` `s` join `college_db`.`courses` `c` where ((`e`.`stude...)

-- Comparison:
-- Before indexing:
-- Full Table Scan on students.

-- After indexing:
-- MySQL uses idx_students_enrollment_year.
-- Fewer rows are examined.
-- Query becomes more efficient.

