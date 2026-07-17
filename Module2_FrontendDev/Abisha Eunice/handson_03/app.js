import { courses } from "./data.js";

/* -------------------------
   ES6 Syntax Practice
--------------------------*/

courses.forEach(course => {

    const { name, credits } = course;

    console.log(`${name} : ${credits} Credits`);

});

const formattedCourses = courses.map(

    ({code,name,credits}) =>

    `${code} - ${name} (${credits} credits)`

);

console.log(formattedCourses);

const filteredCourses = courses.filter(

    course => course.credits >=4

);

console.log("Courses with credits >=4 :",filteredCourses.length);

const totalCredits = courses.reduce(

(previous,current)=>

previous+current.credits

,0);

console.log("Total Credits :",totalCredits);

/* -------------------------
   DOM Selection
--------------------------*/

const grid=document.querySelector(".course-grid");

const total=document.getElementById("total-credits");

const search=document.getElementById("search-courses");

const sortBtn=document.getElementById("sort-btn");

const selected=document.getElementById("selected-course");

/* -------------------------
   Render Function
--------------------------*/

function renderCourses(courseArray){

    grid.innerHTML="";

    courseArray.forEach(course=>{

        const article=document.createElement("article");

        article.className="course-card";

        article.dataset.id=course.id;

        article.innerHTML=`

            <h3>${course.name}</h3>

            <p>Code : ${course.code}</p>

            <p>Credits : ${course.credits}</p>

        `;

        grid.appendChild(article);

    });

    total.textContent=`Total Credits : ${totalCredits}`;

}

renderCourses(courses);

/* -------------------------
   Search
--------------------------*/

search.addEventListener("input",()=>{

    const keyword=search.value.toLowerCase();

    const filtered=courses.filter(course=>

        course.name.toLowerCase().includes(keyword)

    );

    renderCourses(filtered);

});

/* -------------------------
   Sort
--------------------------*/

sortBtn.addEventListener("click",()=>{

    const sorted=[...courses].sort(

        (a,b)=>b.credits-a.credits

    );

    renderCourses(sorted);

});

/* -------------------------
   Event Delegation
--------------------------*/

grid.addEventListener("click",(event)=>{

    const card=event.target.closest(".course-card");

    if(!card) return;

    const id=parseInt(card.dataset.id);

    const course=courses.find(c=>c.id===id);

    selected.textContent=

    `Selected Course : ${course.name}
     | Grade : ${course.grade}`;

});