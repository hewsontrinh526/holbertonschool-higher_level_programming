const redHeader = document.querySelector('#red_header');

redHeader.onclick = colorChange;

function colorChange() {
  let headerElement = document.getElementsByTagName('header')[0];
  headerElement.style.color = '#FF0000';
}
