#!/usr/bin/node

const myvar = process.argv.splice(2);

if (myvar[0] !== undefined) {
  console.log(myvar[2]);
} else {
  console.log('No argument');
}
