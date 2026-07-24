import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCardComponent } from '../course-card/course-card';
import { CourseService, Course } from '../course.service';

@Component({
selector:'app-course-list',
standalone:true,
imports:[CommonModule,FormsModule,CourseCardComponent],
templateUrl:'./course-list.html',
styleUrl:'./course-list.css'
})
export class CourseList implements OnInit{

courses:Course[]=[];
searchTerm='';
loading=true;

constructor(private courseService:CourseService){}

ngOnInit():void{

this.loading=true;

this.courseService.getCourses().subscribe({

next:(data)=>{
this.courses=data;
this.loading=false;
},

error:(err)=>{
console.error(err);
this.loading=false;
}

});

}

get filteredCourses():Course[]{
return this.courses.filter(course=>
course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
);
}

}