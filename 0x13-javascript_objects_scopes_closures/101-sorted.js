#!/usr/bin/node

const dict = require('./101-data').dict;

const numbers = Object.values(dict);
const uniqu = Array.from(new Set(numbers));

const dict2 = {};

uniqu.forEach((val) => {
  const Arr = [];
  for (const i in dict) {
    if (dict[i] === val) {
      Arr.push(i);
    }
  }
  dict2[val] = Arr;
});

console.log(dict2);
