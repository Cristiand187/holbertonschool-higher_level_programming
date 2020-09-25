#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = $('#character');

$.get(url, data => {
  character.text(data.name);
});
