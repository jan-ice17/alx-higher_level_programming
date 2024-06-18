#!/usr/bin/node

// Write a function that prints the number of arguments already printed and the new argument

let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};