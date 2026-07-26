<script setup>

import {useEnrollmentStore} from '../stores/enrollment'

const store=useEnrollmentStore()

</script>


<template>

<header>

<h2>
Student Portal
</h2>


<nav>

<RouterLink to="/">
Home
</RouterLink>

<RouterLink to="/courses">
Courses
</RouterLink>


<RouterLink to="/profile">
Profile
({{store.enrolledCourses.length}})
</RouterLink>


</nav>

</header>

</template>


<style scoped>

header{

background:#1f4e79;
color:white;
padding:20px;

display:flex;
justify-content:space-between;

}


a{

color:white;
margin:10px;
text-decoration:none;

}

</style>