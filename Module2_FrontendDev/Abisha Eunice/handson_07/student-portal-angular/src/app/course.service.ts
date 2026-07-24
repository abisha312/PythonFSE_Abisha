import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';

export interface Course {
  id:number;
  name:string;
  code:string;
  credits:number;
  grade:string;
}

@Injectable({
  providedIn:'root'
})
export class CourseService{

private http=inject(HttpClient);

private courseNames=[
  "Data Structures",
  "Web Development",
  "Database Management Systems",
  "Operating Systems",
  "Computer Networks"
];

getCourses():Observable<Course[]>{

return this.http
.get<any[]>('https://jsonplaceholder.typicode.com/posts?_limit=5')
.pipe(

map((posts)=>{

return posts.map((post,index)=>({

id:index+1,

name:this.courseNames[index],

code:`CS${101+index}`,

credits:index%2===0?4:3,

grade:["A","A+","B+","A","B"][index]

}));

})

);

}

}