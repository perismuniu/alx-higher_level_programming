#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to get characters based on character URLs
function getCharacters(characterUrls, callback) {
  const characters = [];
  let completedRequests = 0;

  characterUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        characters.push(characterData.name);
      } else {
        console.error(error);
      }

      completedRequests++;
      if (completedRequests === characterUrls.length) {
        callback(characters);
      }
    });
  });
}

// Main function to fetch movie details and characters
request(movieUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    getCharacters(characterUrls, characters => {
      characters.forEach(character => {
        console.log(character);
      });
    });
  } else {
    console.error(error);
  }
});
