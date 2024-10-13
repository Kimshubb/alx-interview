#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

// URL of the Star Wars API for the specific film
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the request to get the movie details
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching the movie data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Received a non-200 status code:', response.statusCode);
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // For each character URL, make a request to get the character's name
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character data:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Error: Received a non-200 status code for character:', charResponse.statusCode);
        return;
      }

      // Parse the character data and log the name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

