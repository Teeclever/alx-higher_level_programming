#!/usr/bin/node

const SquareOne = require('./5-square');

module.exports = class Square extends SquareOne {
  charPrint (c) {
    if (c === undefined) c = 'X';
    const w = c.repeat(this.width);
    const h = `${w}\n`.repeat(this.height).trim();
    console.log(h);
  }
};
