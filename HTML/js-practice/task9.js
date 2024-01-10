// Arrays

let countries = ["Kenya", "Uganda", "Tanzania"];

console.log(countries);


let colors = ["Red", "Blue", "Purple", ["Green", "White", "Yellow"]];

console.log(colors[3][2]);


// Array Methods
let supers = ["Batman", "Aquaman", "Flash", "Superman"];

// returns the index of the specified word
console.log(supers.indexOf("Flash"));

// returns a boolean value to confirm if a word is included or not
console.log(supers.includes("Wonder woman"));

// join turns an array into a string
console.log(supers.join("/"));

// split turns a string into an array
let myString = "Red, Blue, Green";
console.log(myString.split(',' ));


// shift removes the first item in the array and returns it
console.log(supers.shift());

console.log(supers);
// removes the last ement from the array and returns it
console.log(supers.pop());

// adds an item at the end of the array
supers.push("Thor");
console.log(supers);

// unshift adds a value at the beginning of an array
supers.unshift("Black Widow")
console.log(supers);
