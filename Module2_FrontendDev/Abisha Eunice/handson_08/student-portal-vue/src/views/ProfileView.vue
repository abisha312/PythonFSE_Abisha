<script setup>

import {useEnrollmentStore} from '../stores/enrollment'

const store=useEnrollmentStore()

</script>


<template>


<section>


<h2>
Student Profile
</h2>


<h3>
Enrolled Courses
</h3>



<p v-if="store.enrolledCourses.length===0">

No courses enrolled

</p>



<div

v-for="course in store.enrolledCourses"

:key="course.id"

>


<h4>
{{course.name}}
</h4>


<p>
Credits: {{course.credits}}
</p>


<button

@click="store.unenroll(course.id)"

>

Remove

</button>


</div>



<h3>

Total Credits:
{{store.totalCredits}}

</h3>


</section>


</template>