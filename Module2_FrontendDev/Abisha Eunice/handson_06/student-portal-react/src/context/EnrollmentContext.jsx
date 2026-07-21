import { createContext, useState } from "react";


// Create Context
export const EnrollmentContext = createContext();



export function EnrollmentProvider({ children }) {


    const [enrolledCourses, setEnrolledCourses] = useState([]);



    // Add course
    const enrollCourse = (course) => {


        const exists = enrolledCourses.find(

            item => item.id === course.id

        );


        if(!exists){

            setEnrolledCourses([

                ...enrolledCourses,

                course

            ]);

        }

    };



    // Remove course
    const removeCourse = (id) => {


        setEnrolledCourses(

            enrolledCourses.filter(

                course => course.id !== id

            )

        );

    };



    return (

        <EnrollmentContext.Provider

            value={{

                enrolledCourses,

                enrollCourse,

                removeCourse

            }}

        >

            {children}

        </EnrollmentContext.Provider>

    );

}