#!/usr/bin/node

const myvar = process.argv.splice(2);

console.log(`${myvar[0]} is ${myvar[1]}`);
