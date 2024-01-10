#!/usr/bin/node
const fs = require('fs');

const argv = process.argv.splice(2);

if (argv.length !== 3) {
  console.error('Usage ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

try {
  const [fileA, fileB, fileC] = argv;

  const dataA = fs.readFileSync(fileA, 'utf8');
  const dataB = fs.readFileSync(fileB, 'utf8');

  const value = `${dataA}\n${dataB}`;
  fs.writeFileSync(fileC, value);
} catch (err) {
  console.error(`Error ${err.message}`);
  process.exit(1);
}
