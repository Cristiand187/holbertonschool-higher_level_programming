#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    let numMovies = 0;
    const films = JSON.parse(response.body).results;
    for (const Item of films) {
      const filmChars = Item.characters;
      for (const charItem of filmChars) {
        if (charItem.includes('18')) {
          numMovies += 1;
        }
      }
    }
    console.log(numMovies);
  }
});
