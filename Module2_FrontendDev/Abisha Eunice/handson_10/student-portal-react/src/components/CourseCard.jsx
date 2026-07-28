import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";
import { useNavigate } from "react-router-dom";

function CourseCard({ id, title, body }) {

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleEnroll = () => {

        dispatch(
            enroll({
                id,
                title,
                body
            })
        );

        navigate("/profile");

    };

    return (

        <article className="course-card">

            <h3>{title}</h3>

            <p>
                <strong>Course ID:</strong> {id}
            </p>

            <p>{body}</p>

            <button onClick={() => navigate(`/courses/${id}`)}>
                View Details
            </button>

            <button onClick={handleEnroll}>
                Enroll
            </button>

        </article>

    );

}

export default CourseCard;