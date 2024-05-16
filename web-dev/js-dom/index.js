function addItems() {

    let button = document.getElementById("inputButton");
    let inputItem = document.getElementById("inputPlace");
    let shoppingList = document.getElementById("shoppingList");

    button.addEventListener("click", function(){
        let li = document.createElement("li");
        li.appendChild(document.createTextNode(inputItem.value));
        shoppingList.appendChild(li);
    });
}

addItems();