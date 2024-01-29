const addItem = document.querySelector("#add_item");

addItem.onclick = addsList;

function addsList() {
    let listElement = document.querySelector(".my_list");
    let newListItem = document.createElement("li");
    newListItem.textContent = "Item";
    listElement.appendChild(newListItem);
}