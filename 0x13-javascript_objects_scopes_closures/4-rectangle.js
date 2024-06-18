#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let a = 0; a < this.height; a++) {
        let d = '';
        for (let b = 0; b < this.width; b++) {
          d += 'X';
        }
        console.log(d);
      }
    }
  
    rotate () {
      const exc = this.width;
      this.width = this.height;
      this.height = exc;
    }
  
    double () {
      this.width *= 2;
      this.height *= 2;
    }
  }
  
  module.exports = Rectangle;
  