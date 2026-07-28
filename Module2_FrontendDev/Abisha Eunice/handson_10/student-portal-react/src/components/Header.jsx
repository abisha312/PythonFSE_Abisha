import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

function Header({ siteName }) {
    const enrolledCourses = useSelector(
        state => state.enrollment.enrolledCourses
    );

    return (
        <header>
            <h2 className="site-title">{siteName}</h2>

            <nav>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/courses">Courses</Link>
                    </li>
                    <li>
                        <Link to="/profile">Profile</Link>
                    </li>
                </ul>
            </nav>

            <div className="enrollment-count">
                Enrolled: {enrolledCourses.length}
            </div>
        </header>
    );
}

export default Header;