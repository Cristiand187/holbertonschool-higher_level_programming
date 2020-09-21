#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (character = 'X') {
    for (let i = 0; i < this.height; i++) {
      let cadena = '';
      for (let j = 0; j < this.width; j++) {
        cadena += character;
      }
      console.log(cadena);
    }
  }
};
