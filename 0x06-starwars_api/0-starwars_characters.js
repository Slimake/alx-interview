#!/usr/bin/node
const request = require('request');

const arg = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${arg}/`;

// Wrap the request in a Promise
function requestPromise (options) {
  return new Promise((resolve, reject) => {
    request(options, (error, response, body) => {
      if (error) reject(error);
      if (response && response.statusCode === 200) {
        resolve(body);
      }
    });
  });
}

async function fetchData () {
  try {
    // Await the request wrapped in a promise
    const response = await requestPromise({ url, json: true });
    const promises = response.characters.map(url => {
      return requestPromise({ url, json: true });
    });

    const responses = await Promise.all(promises);
    responses.forEach(response => {
      console.log(response.name);
    });
  } catch (error) {
    console.log(error);
  }
}

fetchData();
