// TASK 1
// let userInput = prompt("Please enter your name: ");

// if (userInput === "James" || userInput === "Mike"){
//     alert("Hi James or Mike!");
// }

// function greedPerson(){
//     console.log("Hello " + userInput);
// }

// var sayGoodbye = function(){
//     console.log("Bye");
// }


// if (userInput === "James") {
//     alert("Hi James");
// } 
// else if (userInput === "Mike") {
//     alert("Hi Mike!");
// }

// greedPerson();
// sayGoodbye();


// TASK 2
function checkAge(){
    let userAge = prompt("Please enter your age: ");

    if (userAge > 18) {
        console.log("The car is ready!");
    }
    else if (userAge == 18) {
        console.log("First year driving. Enjoy your ride!");
    }
    else if (userAge => 1 & userAge < 18) {
        console.log("You can't drive this car. Sorry.");
    }
    else if (userAge < 1) {
        console.log("Interesting age.");
    }
}

checkAge();