#!/usr/bin/node
const request = require('request');

const arg = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${arg}/`;
request(url, (error, response, body) => {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    data.characters.forEach(url => {
      request(url, (error, response, body) => {
        if (error) console.log(error);
        else if (response.statusCode === 200) {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    });
  }
});
