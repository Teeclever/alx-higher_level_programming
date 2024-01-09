#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(this.validate(w, h))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const w = 'X'.repeat(this.width);
    const h = `${w}\n`.repeat(this.height).trim();
    console.log(h);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  validate (w, h) {
    if ((w <= 0 || h <= 0) || (w === undefined || h === undefined)) {
      return true;
    }
  }
};
