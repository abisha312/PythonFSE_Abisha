import { createSlice } from "@reduxjs/toolkit";


const initialState = {

    enrolledCourses: []

};


const enrollmentSlice = createSlice({

    name: "enrollment",

    initialState,

    reducers: {


        enroll: (state, action) => {

            const courseExists = state.enrolledCourses.find(

                course => course.id === action.payload.id

            );


            if(!courseExists){

                state.enrolledCourses.push(action.payload);

            }

        },


        unenroll: (state, action) => {

            state.enrolledCourses = state.enrolledCourses.filter(

                course => course.id !== action.payload

            );

        }


    }

});


// Export actions
export const { enroll, unenroll } = enrollmentSlice.actions;


// Export reducer
export default enrollmentSlice.reducer;