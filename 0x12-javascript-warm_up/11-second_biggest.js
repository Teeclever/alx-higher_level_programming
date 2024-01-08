#!/usr/bin/node
const { argv } = require('process');

// Check if there are fewer than 3 arguments (script name + 1 argument)
if (argv.length <= 3) {
  console.log('0'); // Print '0' since there are not enough arguments to find the second largest
} else {
  let numsSorted = []; // Initialize an empty array to store sorted numbers
  for (let n = 2; n < argv.length; n++) {
    const curr = parseInt(argv[n]); // Convert the current argument to an integer
    numsSorted = insertSorted(curr, numsSorted); // Insert the current number into the sorted array
  }
  console.log(numsSorted[(numsSorted.length) - 2]); // Print the second largest number
}

// Function to insert a number into a sorted array while maintaining the sorting
function insertSorted (num, arr) {
  if (!arr) {
    return [num]; // If the array is empty, simply return an array containing the number
  }

  for (let n = 0; n < arr.length; n++) {
    if (arr[n] >= num) { // Find the position where the current number should be inserted
      return [...arr.slice(0, n), num, ...arr.slice(n)]; // Insert the number while preserving sorting
    }
  }

  return [...arr, num]; // If the number should be inserted at the end, append it
}
