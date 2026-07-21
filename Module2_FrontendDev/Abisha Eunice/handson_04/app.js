import { courses } from "./data.js";


const grid = document.querySelector(".course-grid");

const total = document.getElementById("total-credits");

const search = document.getElementById("search-courses");

const sortBtn = document.getElementById("sort-btn");

const selected = document.getElementById("selected-course");

const loadingCourses = document.getElementById("loading-courses");

const notificationList = document.getElementById("notification-list");

const loadingSpinner = document.getElementById("loading-spinner");

const errorMessage = document.getElementById("error-message");

const retryBtn = document.getElementById("retry-btn");



courses.forEach(({ name, credits }) => {

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

    (sum, course) => sum + course.credits,

    0

);

console.log("Total Credits :", totalCredits);


function updateTotalCredits(courseArray) {

    const credits = courseArray.reduce(

        (sum, course) => sum + course.credits,

        0

    );

    total.textContent = `Total Credits : ${credits}`;

}


function showCourseLoading() {

    loadingCourses.hidden = false;

}


function hideCourseLoading() {

    loadingCourses.hidden = true;

}


function showSpinner() {

    loadingSpinner.hidden = false;

}


function hideSpinner() {

    loadingSpinner.hidden = true;

}


function renderCourses(courseArray) {

    grid.innerHTML = "";

    const fragment = document.createDocumentFragment();

    courseArray.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `

            <h3>${course.name}</h3>

            <p><strong>Code:</strong> ${course.code}</p>

            <p><strong>Credits:</strong> ${course.credits}</p>

        `;

        fragment.appendChild(article);

    });

    grid.appendChild(fragment);

    updateTotalCredits(courseArray);

}



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



grid.addEventListener("click", event => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const id = Number(card.dataset.id);

    const course = courses.find(c => c.id === id);

    selected.textContent =

        `Selected Course : ${course.name} | Grade : ${course.grade}`;

});


// Requirement 45
// Promise Chaining

function fetchUser(id) {

    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(response => response.json())
        .then(user => {

            console.log("Promise User :", user.name);

            return user;

        });

}

fetchUser(1);


// Requirement 46
// async / await

async function fetchUserAsync(id) {

    try {

        const response = await fetch(
            `https://jsonplaceholder.typicode.com/users/${id}`
        );

        const user = await response.json();

        console.log("Async User :", user.name);

        return user;

    }

    catch (error) {

        console.error(error);

    }

}

fetchUserAsync(2);


// Requirement 47

function fetchAllCourses() {

    return new Promise(resolve => {

        setTimeout(() => {

            resolve(courses);

        }, 1000);

    });

}


// Requirement 48

async function loadCourses() {

    showCourseLoading();

    const courseList = await fetchAllCourses();

    hideCourseLoading();

    renderCourses(courseList);

}

loadCourses();


// Requirement 49

Promise.all([

    fetchUser(1),

    fetchUser(2)

]).then(users => {

    console.log("Promise.all Users");

    users.forEach(user =>

        console.log(user.name)

    );

});



async function apiFetch(url) {

    const response = await fetch(url);

    if (!response.ok) {

        throw new Error("Unable to fetch data.");

    }

    return await response.json();

}



function renderNotifications(posts) {

    notificationList.innerHTML = "";

    posts.slice(0, 10).forEach(post => {

        const article = document.createElement("article");

        article.className = "notification-card";

        article.innerHTML = `

            <h3>${post.title}</h3>

            <p>${post.body}</p>

        `;

        notificationList.appendChild(article);

    });

}



async function loadNotifications() {

    try {

        errorMessage.textContent = "";

        retryBtn.hidden = true;

        showSpinner();

        const posts = await apiFetch(

            "https://jsonplaceholder.typicode.com/posts"

        );

        hideSpinner();

        renderNotifications(posts);

    }

    catch (error) {

        hideSpinner();

        errorMessage.textContent =

            "Unable to load notifications.";

        retryBtn.hidden = false;

    }

}

loadNotifications();


//REQUIREMENT 53

async function simulate404() {

    try {

        await apiFetch(

            "https://jsonplaceholder.typicode.com/nonexistent"

        );

    }

    catch (error) {

        errorMessage.textContent =

            "404 Error : Resource not found.";

        retryBtn.hidden = false;

    }

}


// simulate404();


//REQUIREMENT 54

retryBtn.addEventListener("click", () => {

    errorMessage.textContent = "";

    retryBtn.hidden = true;

    loadNotifications();

});


/*
Difference between Fetch and Axios

1. Fetch is built into browsers.
   Axios requires installation/CDN.

2. Fetch needs response.json().
   Axios automatically converts JSON.

3. Fetch does not reject HTTP errors.
   Axios automatically throws errors.
*/


axios.interceptors.request.use(config => {

    console.log(

        `API call started : ${config.url}`

    );

    return config;

});


async function apiFetchAxios(url) {

    try {

        const response = await axios.get(

            url,

            {

                timeout:5000

            }

        );

        return response.data;

    }

    catch(error){

        throw error;

    }

}


async function loadAxiosPosts(){

    try{

        const posts = await axios.get(

            "https://jsonplaceholder.typicode.com/posts",

            {

                params:{

                    userId:1

                }

            }

        );

        console.log(

            "Axios User 1 Posts",

            posts.data

        );

    }

    catch(error){

        console.log(error);

    }

}

loadAxiosPosts();
