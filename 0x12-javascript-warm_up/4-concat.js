#!/usr/bin/node
const concatString = process.argv;

if (concatString[2]) {
  console.log(concatString[2] + ' is ' + concatString[3]);
} else {
  console.log('undefined is undefined');
}
