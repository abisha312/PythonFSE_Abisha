import { useParams } from "react-router-dom";
import coursesData from "../data/courses";

function CourseDetailPage() {

    const { courseId } = useParams();

    const course = coursesData.find(
        c => c.id === Number(courseId)
    );

    if (!course) {
        return <h2>Course not found</h2>;
    }

    return (
        <section>

            <h2>{course.name}</h2>

            <p>Code: {course.code}</p>

            <p>Credits: {course.credits}</p>

            <p>Grade: {course.grade}</p>

        </section>
    );
}

export default CourseDetailPage;