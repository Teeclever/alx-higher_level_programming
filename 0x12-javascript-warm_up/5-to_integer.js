#!/usr/bin/node

const myvar = process.argv.splice(2);

if (Number.isInteger(parseInt(myvar[0]))) {
  console.log(`My number: ${parseInt(myvar[0])}`);
} else {
  console.log('Not a number');
}
