#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) {
    return console.error(err);
  } else {
    console.log(data.toString());
  }
});
