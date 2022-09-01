#!/usr/bin/node
// return of the jedi

const request = require('request');
const FILMID = process.argv[2];

// same order
const URL_BASE = 'https://swapi-api.hbtn.io/api/films';

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}

// characters list

async function main (filmID) {
  const res = await doRequest(`${URL_BASE}/${filmID}`);
  const promesas = res.characters.map(url => doRequest(url));

  try {
    const personajes = await Promise.all(promesas);
    const names = personajes.map(pj => pj.name);
    console.log(names.join('\n'));
  } catch (error) {
    console.log(error);
  }
}

main(FILMID);
