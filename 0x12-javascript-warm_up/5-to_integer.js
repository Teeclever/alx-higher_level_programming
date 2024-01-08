#!/usr/bin/node
const { argv } = require('process');

if (!argv[2] || !parseInt(argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(argv[2])}`);
}
