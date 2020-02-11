#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body);
    const toReturn = {};
    for (let i = 0; i < results.length; i++) {
      if (results[i].userId in toReturn) {
        if (results[i].completed) {
          toReturn[results[i].userId]++;
        }
      } else if (results[i].completed) {
        toReturn[results[i].userId] = 1;
      }
    }
    console.log(toReturn);
  }
});
