#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(this.validate(w, h))) {
      this.width = w;
      this.height = h;
    }
  }

  validate (w, h) {
    if ((w <= 0 || h <= 0) || (w === undefined || h === undefined)) {
      return true;
    }
  }
};
