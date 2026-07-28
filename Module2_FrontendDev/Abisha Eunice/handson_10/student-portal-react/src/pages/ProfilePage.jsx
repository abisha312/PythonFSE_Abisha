import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {

    const enrolledCourses = useSelector(
        state => state.enrollment.enrolledCourses
    );

    const dispatch = useDispatch();

    return (
        <section>

            <h2>Student Profile</h2>

            <h3>
                Enrolled Courses
            </h3>

            {
                enrolledCourses.length === 0 ? (
                    <p>No courses enrolled</p>
                ) : (

                    enrolledCourses.map(course => (

                        <div 
                            key={course.id}
                            className="course-card"
                        >

                            <h4>{course.name}</h4>

                            <p>{course.code}</p>

                            <button
                                onClick={() =>
                                    dispatch(unenroll(course.id))
                                }
                            >
                                Remove
                            </button>

                        </div>

                    ))

                )
            }

        </section>
    );
}

export default ProfilePage;