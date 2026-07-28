import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import CourseCard from "../components/CourseCard";
import {
    fetchAllCourses,
    selectCourses,
    selectCoursesLoading,
    selectCoursesError
} from "../redux/enrollmentSlice";

function CoursesPage() {

    const dispatch = useDispatch();

    const courses = useSelector(selectCourses);
    const loading = useSelector(selectCoursesLoading);
    const error = useSelector(selectCoursesError);

    const [searchTerm, setSearchTerm] = useState("");

    useEffect(() => {

        dispatch(fetchAllCourses());

    }, [dispatch]);

    const filteredCourses = courses.filter(course =>
        course.title.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <section id="courses">

            <h2>Available Courses</h2>

            <input
                type="text"
                placeholder="Search courses..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />

            {loading && <p>Loading courses...</p>}

            {error && <p>Error: {error}</p>}

            <div className="course-grid">

                {filteredCourses.map(course => (
                    <CourseCard
                        key={course.id}
                        id={course.id}
                        title={course.title}
                        body={course.body}
                    />
                ))}

            </div>

        </section>
    );
}

export default CoursesPage;