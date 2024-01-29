const header = document.querySelector("#toggle_header");

header.onclick = toggleClass;

function toggleClass() {
    let element = document.getElementsByTagName("header")[0];
    element.classList.toggle("red");
    element.classList.toggle("green")
}