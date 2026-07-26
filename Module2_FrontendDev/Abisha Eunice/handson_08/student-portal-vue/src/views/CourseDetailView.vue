<script setup>

import {useRoute,useRouter} from 'vue-router'
import {useEnrollmentStore} from '../stores/enrollment'


const route=useRoute()

const router=useRouter()

const store=useEnrollmentStore()



const courses=[

{
id:1,
name:"Data Structures",
credits:4
},

{
id:2,
name:"Web Development",
credits:3
},

{
id:3,
name:"Database Systems",
credits:4
}

]


const course=

courses.find(

c=>c.id==route.params.id

)



function enroll(){

store.enroll(course)

router.push('/profile')

}


</script>



<template>


<section>


<h2>

{{course?.name}}

</h2>


<p>

Credits:
{{course?.credits}}

</p>


<button @click="enroll">

Enroll

</button>


</section>


</template>