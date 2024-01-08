#!/usr/bin/node
const { argv } = require('process');

const num = parseInt(argv[2]);
console.log(factorial(num));

function factorial (num) {
  if (!num) {
    return 1;
  }
  return num * factorial(num - 1);
}
