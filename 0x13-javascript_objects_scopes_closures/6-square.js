#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) c = 'X';
    const w = c.repeat(this.width);
    const h = `${w}\n`.repeat(this.height).trim();
    console.log(h);
  }
};
