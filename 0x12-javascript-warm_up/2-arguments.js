#!/usr/bin/node
const { argv } = require('process');
const argLen = argv.length;

if (argLen === 2) {
  console.log('No argument');
} else if (argLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
