// Date object

let currentDate = new Date();
// console.log(currentDate);


// let date = currentDate.getDate();
// let day = currentDate.getDay();
// let year = currentDate.getFullYear();
// let month = currentDate.getMonth();

// console.log(date);
// console.log(day);
// console.log(year);
// console.log(month);


// gets the current date and console logs it
let date = new Date();
console.log(date);

let hour = date.getHours();
let min = date.getMinutes();

console.log(`${hour}:${min}`);

let day = date.toLocaleString("default", {weekday: "short"});
console.log(day);