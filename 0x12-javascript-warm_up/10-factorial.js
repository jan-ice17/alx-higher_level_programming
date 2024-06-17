#!/usr/bin/node

// Write a script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer)
// You must do it recursively

function factorial (x) {
  return x === 0 || isNaN(x) ? 1 : x * factorial(x - 1);
}

console.log(factorial(Number(process.argv[2])));
