import { courses } from "./data.js";


courses.forEach(course => {
    const { name, credits } = course;
    console.log(`${name} : ${credits} Credits`);
});

const formattedCourses = courses.map(
    ({ code, name, credits }) =>
        `${code} - ${name} (${credits} credits)`
);

console.log(formattedCourses);

const filteredCourses = courses.filter(
    course => course.credits >= 4
);

console.log("Courses with credits >= 4 :", filteredCourses.length);

const totalCredits = courses.reduce(
    (previous, current) => previous + current.credits,
    0
);

console.log("Total Credits :", totalCredits);


const grid = document.querySelector(".course-grid");
const total = document.getElementById("total-credits");
const search = document.getElementById("search-courses");
const sortBtn = document.getElementById("sort-btn");
const selected = document.getElementById("selected-course");
const courseCount = document.getElementById("course-count");


function renderCourses(courseArray) {

    grid.innerHTML = "";

    courseCount.textContent = `${courseArray.length} courses found`;

    courseArray.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";
        article.dataset.id = course.id;

        article.setAttribute("tabindex", "0");
        article.setAttribute("role", "button");
        article.setAttribute("aria-label", `${course.name} course`);

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code : ${course.code}</p>
            <p>Credits : ${course.credits}</p>
        `;

        article.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                article.click();
            }
        });

        grid.appendChild(article);

    });

    total.textContent = `Total Credits : ${totalCredits}`;

}

renderCourses(courses);


search.addEventListener("input", () => {

    const keyword = search.value.toLowerCase();

    const filtered = courses.filter(course =>
        course.name.toLowerCase().includes(keyword)
    );

    renderCourses(filtered);

});


sortBtn.addEventListener("click", () => {

    const sorted = [...courses].sort(
        (a, b) => b.credits - a.credits
    );

    renderCourses(sorted);

});


grid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const id = Number(card.dataset.id);

    const course = courses.find(c => c.id === id);

    if (!course) return;

    selected.textContent =
        `Selected Course : ${course.name} | Code : ${course.code} | Credits : ${course.credits} | Grade : ${course.grade}`;

});


document.addEventListener("keydown", (event) => {

    if (event.key === "Escape") {

        selected.textContent = "";

    }

});