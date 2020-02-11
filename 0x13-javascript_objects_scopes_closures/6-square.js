#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let charToPrint = '';
      for (let j = 0; j < this.width; j++) {
        charToPrint += c;
      }
      console.log(charToPrint);
    }
  }
}
module.exports = Square;
