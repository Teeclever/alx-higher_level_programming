#!/usr/bin/node
const argLen = process.argv.splice(2).length;

if (argLen === 0) {
  console.log('No argument');
} else if (argLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
