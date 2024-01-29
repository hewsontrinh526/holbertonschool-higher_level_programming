const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = document.querySelector('#character');

async function fetchName() {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data.name);
    character.textContent = data.name;
}
