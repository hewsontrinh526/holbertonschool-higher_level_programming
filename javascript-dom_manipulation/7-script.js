const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.querySelector('#list_movies');

async function fetchMovies() {
  const response = await fetch(url);
  const data = await response.json();
  const movies = data.results;

  for (const movie of movies) {
    const newMovie = document.createElement('li');
    newMovie.textContent = movie.title;
    listMovies.appendChild(newMovie);
  }
}

fetchMovies();
