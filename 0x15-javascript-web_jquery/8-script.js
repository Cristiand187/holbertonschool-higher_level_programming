#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const ul = $('#list_movies');

$.get(url, data => {
  data.results.forEach(films => {
    ul.append('<li>' + films.title + '</li>');
  });
});
