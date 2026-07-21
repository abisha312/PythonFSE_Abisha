import { useState, useEffect } from "react";
import "./App.css";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

import { courses as localCourses } from "./data/courses";

function App() {

  const [courses, setCourses] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");


  useEffect(() => {

    async function fetchCourses() {

      try {

        setLoading(true);

        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

        if (!response.ok) {

          throw new Error("Unable to fetch courses.");

        }

        const data = await response.json();

        const apiCourses = data.slice(0, 5).map((post, index) => ({

          id: post.id,

          name: localCourses[index].name,

          code: localCourses[index].code,

          credits: localCourses[index].credits,

          grade: localCourses[index].grade

        }));

        setCourses(apiCourses);

      }

      catch (err) {

        setError(err.message);

      }

      finally {

        setLoading(false);

      }

    }

    fetchCourses();

  }, []);

  useEffect(() => {

    console.log("Courses updated");

  }, [courses]);


  function handleEnroll(course) {

    const alreadyExists = enrolledCourses.some(

      c => c.id === course.id

    );

    if (alreadyExists) {

      alert("Already Enrolled!");

      return;

    }

    setEnrolledCourses(

      [...enrolledCourses, course]

    );

  }


  const filteredCourses = courses.filter(course =>

    course.name
      .toLowerCase()
      .includes(searchTerm.toLowerCase())

  );



  if (loading) {

    return (

      <div className="loading">

        <h2>Loading...</h2>

      </div>

    );

  }



  if (error) {

    return (

      <div className="error">

        <h2>{error}</h2>

      </div>

    );

  }


  return (

    <>

      <Header

        siteName="Student Portal"

        enrolledCount={enrolledCourses.length}

      />



      <main className="container">

        <section className="hero">

          <h1>Welcome to Student Portal</h1>

          <p>

            Browse courses, enroll, and update your profile.

          </p>

        </section>



        <section>

          <input

            className="search"

            type="text"

            placeholder="Search Courses..."

            value={searchTerm}

            onChange={(e) =>

              setSearchTerm(e.target.value)

            }

          />

        </section>



        <section className="course-grid">

          {

            filteredCourses.length === 0 ?

              (

                <h3>

                  No Courses Found

                </h3>

              )

              :

              (

                filteredCourses.map(course => (

                  <CourseCard

                    key={course.id}

                    {...course}

                    onEnroll={handleEnroll}

                  />

                ))

              )

          }

        </section>



        <StudentProfile />

      </main>



      <Footer />

    </>

  );

}

export default App;