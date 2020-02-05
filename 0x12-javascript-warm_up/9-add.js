#!/usr/bin/node
if (parseInt(process.argv[2]) && parseInt(process.argv[3])) {
    console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
  } else {
    console.log('NaN');
  }
  function add (a, b) {
    return a + b;
  }
