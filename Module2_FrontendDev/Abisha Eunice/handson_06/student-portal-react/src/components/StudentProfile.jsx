import { useState } from "react";

function StudentProfile() {

    const [student, setStudent] = useState({

        name: "Abisha Eunice",
        email: "abisha@example.com",
        semester: "6"

    });

    function handleChange(event) {

        const { name, value } = event.target;

        setStudent(prev => ({

            ...prev,

            [name]: value

        }));

    }

    return (

        <div className="profile">

            <h2>Student Profile</h2>

            <form>

                <label>Name</label>

                <input
                    type="text"
                    name="name"
                    value={student.name}
                    onChange={handleChange}
                />

                <label>Email</label>

                <input
                    type="email"
                    name="email"
                    value={student.email}
                    onChange={handleChange}
                />

                <label>Semester</label>

                <input
                    type="number"
                    name="semester"
                    value={student.semester}
                    onChange={handleChange}
                />

            </form>

            <div className="profile-preview">

                <h3>Preview</h3>

                <p><strong>Name:</strong> {student.name}</p>

                <p><strong>Email:</strong> {student.email}</p>

                <p><strong>Semester:</strong> {student.semester}</p>

            </div>

        </div>

    );

}

export default StudentProfile;