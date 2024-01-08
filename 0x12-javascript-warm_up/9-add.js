#!/usr/bin/node

const times = process.argv.splice(2);

function add (a, b) {
  return a + b;
}

if (Number.isInteger(parseInt(times[0])) && Number.isInteger(parseInt(times[1]))) {
  console.log(add(times[0], times[1]));
} else {
  console.log(NaN);
}
