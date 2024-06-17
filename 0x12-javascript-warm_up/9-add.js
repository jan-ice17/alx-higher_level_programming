#!/usr/bin/node

// Write a script that prints the addition of 2 integers

// The first argument is the first integer
// The second argument is the second integer
// You have to define a function with this prototype: function add(a, b)

const argv = process.argv;
const add = (a, b) => a + b;

console.log(add(+argv[2], +argv[3]));
