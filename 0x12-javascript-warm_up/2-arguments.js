#!/usr/bin/node

const myvar = process.argv.splice(2);

if (myvar.length > 0) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
