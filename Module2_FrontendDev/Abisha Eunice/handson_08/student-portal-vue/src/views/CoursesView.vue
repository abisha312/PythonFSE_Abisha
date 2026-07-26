<script setup>

import {ref,computed,onMounted} from 'vue'
import CourseCard from '../components/CourseCard.vue'
import {useEnrollmentStore} from '../stores/enrollment'


const store=useEnrollmentStore()


const courses=ref([])

const searchTerm=ref("")


onMounted(()=>{


courses.value=[

{
id:1,
name:"Data Structures",
code:"CS101",
credits:4,
grade:"A"
},

{
id:2,
name:"Web Development",
code:"CS102",
credits:3,
grade:"A+"
},

{
id:3,
name:"Database Systems",
code:"CS103",
credits:4,
grade:"B+"
},

{
id:4,
name:"Operating Systems",
code:"CS104",
credits:4,
grade:"A"
},

{
id:5,
name:"Computer Networks",
code:"CS105",
credits:3,
grade:"B"
}

]


})


const filteredCourses=computed(()=>{


return courses.value.filter(course=>

course.name
.toLowerCase()
.includes(
searchTerm.value.toLowerCase()
)

)


})


function enrollCourse(course){

store.enroll(course)

}


</script>



<template>


<section>


<h2>
Available Courses
</h2>


<input

v-model="searchTerm"

placeholder="Search courses..."

>



<div class="course-grid">


<CourseCard

v-for="course in filteredCourses"

:key="course.id"

:name="course.name"

:code="course.code"

:credits="course.credits"

:grade="course.grade"

@enroll="enrollCourse(course)"

>


</CourseCard>


</div>



<p v-if="filteredCourses.length===0">

No courses found

</p>



</section>


</template>



<style scoped>

.course-grid{

display:grid;

grid-template-columns:
repeat(auto-fit,minmax(250px,1fr));

gap:20px;

margin-top:20px;

}

input{

padding:10px;

width:100%;

}

</style>