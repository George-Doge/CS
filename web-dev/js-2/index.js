let databaza = [{
    username:"Matej",
    passwd:"heslo",
},{
    username:"Heslo",
    passwd: "patrik",
},{
    username:"Maros",
    passwd:"Snina",
}]


let userNameInput = prompt("Zadaj pouzivatelske meno: ");
let passwdInput = prompt("Zadaj heslo: ");


function validUser(meno, heslo, databaza){
    for (let i = 0; i < databaza.length; i++) {
        if(meno === databaza[i].username && heslo === databaza[i].passwd) {
            return true;
        }
    }
    return false;
}

console.log(validUser(userNameInput, passwdInput, databaza));