const header = document.querySelector("#update_header");

header.onclick = updateHeader;

function updateHeader() {
    let newText = document.querySelector("header");
    newText.textContent = "NEW HEADER!!!"
}
