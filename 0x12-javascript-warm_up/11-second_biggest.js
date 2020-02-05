#!/usr/bin/node
const array = [];
if (process.argv.length === 2 || !process.argv[3]) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    array[i - 2] = parseInt(process.argv[i]);
  }
  array.sort(function (a, b) {
    return b - a;
  });
  console.log(array[1]);
}
