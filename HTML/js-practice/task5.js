// string methods


// changes the string to uppercase
let x = "   I am watching Dev Dreamer  ";
let cap = x.toLocaleUpperCase();
console.log(cap);

// removes leading and tailing white spaces from a string
let short = x.trim();
console.log(short);

// changes string to lower case
let lower = x.toLocaleLowerCase();
console.log(lower);

// extracts a specified portion of the string
let newString = x.slice(17, 28);
console.log(newString);