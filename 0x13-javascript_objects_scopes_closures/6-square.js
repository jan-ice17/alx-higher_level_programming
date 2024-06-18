#!/usr/bin/node

// Write a class Square that defines a square and inherits from Square of 5-square.js

const SquareSix = require('./5-square');

class Square extends SquareSix {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let k = 0; k < this.height; k++) {
      let h = '';
      for (let m = 0; m < this.width; m++) {
        h += c;
      }
      console.log(h);
    }
  }
}

module.exports = Square;