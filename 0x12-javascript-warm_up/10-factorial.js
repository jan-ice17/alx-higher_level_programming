#!/usr/bin/node

// Write a script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer)
// You must do it recursively

function factorial (n) {
    if (n < 0) {
      return 1;
    } else if (n === 0) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  
  const firstAgrs = process.argv[2];
  const num = Number(firstAgrs);
  
  if (!Number.isInteger(num)) {
    console.log(num);
  } else {
    const factorialResult = factorial(num);
    console.log(factorialResult);
  }
  