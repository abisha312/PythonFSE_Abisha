import { useState } from "react";
import CourseCard from "../components/CourseCard";
import coursesData from "../data/courses";

function CoursesPage() {
    const [searchTerm, setSearchTerm] = useState("");

    const filteredCourses = coursesData.filter(course =>
        course.name.toLowerCase().includes(searchTerm.toLowerCase())
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

            <div className="course-grid">
                {filteredCourses.map(course => (
                    <CourseCard
                        key={course.id}
                        {...course}
                    />
                ))}
            </div>
        </section>
    );
}

export default CoursesPage;