<script setup>


defineProps({

name:String,

code:String,

credits:Number,

grade:String

})


</script>



<template>


<div class="card">


<h3>
{{name}}
</h3>


<p>
Code: {{code}}
</p>


<p>
Credits: {{credits}}
</p>


<p>
Grade: {{grade}}
</p>


<button @click="$emit('enroll')">

Enroll

</button>


<button @click="$router.push('/courses/'+code)">

View Details

</button>


</div>


</template>



<style scoped>

.card{

background:white;

padding:20px;

border-radius:10px;

box-shadow:0 2px 8px #ccc;

}


button{

margin:5px;

padding:8px;

cursor:pointer;

}

</style>