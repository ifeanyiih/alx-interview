#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + movieID +'/', async function (error,
response, body) {
    if (error) console.log(error);
    film = JSON.parse(body);

    function handleCharacters(url) {
        return new Promise((resolve, reject) => {
            request(url, (error, response, body) => {
                if (error) reject(error);
                const character = JSON.parse(body);
                resolve(character.name);
            })
        })
    }

    characters = film.characters;
    for (const character of characters) {
        const name = await handleCharacters(character);
        console.log(name);
    }
});
