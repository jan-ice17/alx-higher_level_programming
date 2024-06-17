#!/usr/bin/node

// Write a script that prints x times “C is fun”

const x = process.argv[2];

const nums = Number(x);

if (Number.isInteger(nums)) {
  for (let i = 0; i < nums; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
