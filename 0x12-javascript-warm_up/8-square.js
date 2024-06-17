#!/usr/bin/node

// Write a script that prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// You must use the character X to print the square

const firstArgs = process.argv[2];
const num = Number(firstArgs);

if (Number.isInteger(num)) {
  let line = '';
  for (let j = 0; j < num; j++) {
    line += 'X'; // Print the line of 'X's
  }
  console.log(line);
} else {
  console.log('Missing size');
}
