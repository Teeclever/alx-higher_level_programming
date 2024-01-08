#!/usr/bin/node
const myvar = process.argv.splice(2);

if (!myvar[0]) {
  console.log('No argument');
} else {
  console.log(myvar[0]);
}
