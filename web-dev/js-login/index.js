let username = document.getElementById("loginMeno");
let passwd = document.getElementById("loginHeslo");
let button = document.getElementById("enter");
let message = document.getElementById("sprava");

let databaza = [
    {user:"jana", passwd:"heslo"},
    {user:"matej", passwd:"123456789"},
    {user:"dano", passwd:"phasmo"}
];
    
button.addEventListener("click", function() {
    let un = username.value;
    let p = passwd.value;

    let match = databaza.find(object => object.user === un);

    if (match) {
        if (match.passwd === p) {
            message.innerHTML = "Prihlásenie bolo úspešné!";
        } else {
            message.innerHTML = "Nesprávne heslo!";
        }
    }
    else {
        message.innerHTML = "Tento účet neexistuje!";
    }

    username.value = "";
    passwd.value = "";

});