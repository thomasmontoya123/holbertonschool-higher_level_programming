#!/usr/bin/node
const request = require('request');
let counter = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body).results;
    let movie;
    let character;
    for (movie of results) {
      for (character of movie.characters) {
        if (character === 'https://swapi.co/api/people/18/') {
          counter++;
        }
      }
    }
  }
  console.log(counter);
}
);
