#!/usr/bin/node
let x = '';
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    x = '';
    for (let j = 0; j < process.argv[2]; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
