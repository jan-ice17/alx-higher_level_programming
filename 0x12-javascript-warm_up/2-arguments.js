#!/usr/bin/node

// Write a script that prints a message depending of the number of arguments passed:
// If no arguments are passed to the script, print “No argument”
// If only one argument is passed to the script, print “Argument found”
// Otherwise, print “Arguments found”
// You must use console.log(...) to print all output
// You are not allowed to use var Reference: process.argv
 
const argv = process.argv;

if (argv.length === 2) {
  console.log('No argument');  // no arg is found
} else if (argv.length === 3) {
  console.log('Argument found'); // only one arg
} else {
  console.log('Arguments found');
}
