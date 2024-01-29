document.addEventListener('DOMContentLoaded', function () {
  async function fetchHello() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    const selectHello = document.getElementById('hello');
    const response = await fetch(url);
    const data = await response.json();

    selectHello.textContent = data.hello;
  }

  fetchHello();
});
