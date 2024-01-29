const header = document.querySelector('#red_header');

header.onclick = colorChange;

function colorChange() {
  let headerElement = document.getElementsByTagName('header')[0];
  headerElement.classList.add('red');
}
