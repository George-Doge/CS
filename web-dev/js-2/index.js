let databaza = [{
    username:"Matej",
    passwd:"heslo",
    age:true
},{
    username:"Patrik",
    passwd: "realneTazkeHeslo",
    age: false
},{
    username:"Maros",
    passwd:"Snina",
    age:true
}]


let userNameInput = prompt("Zadaj pouzivatelske meno: ");
let passwdInput = prompt("Zadaj heslo: ");


function validUser(meno, heslo, databaza){
    for (var i = 0; i < databaza.length; i++) {
        if(meno === databaza[i].username && heslo === databaza[i].passwd) {
            return true;
        }
    }
    return false;
}
    
console.log(validUser(userNameInput, passwdInput, databaza));