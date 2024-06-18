#!/usr/bin/node

/**
 * CWrite a class Rectangle that defines a rectangle:heck the parameters provided
 */

class Rectangle {
    constructor (w, h) {
      if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        let myVariable= '';
        let y = 0;
        while (y < this.width) {
          myVariable+= 'X';
          y++;
        }
  
        console.log(myVariable);
      }
    }
  }
  module.exports = Rectangle;
