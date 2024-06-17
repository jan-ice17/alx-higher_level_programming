#!/usr/bin/node

// Write a script that prints a message depending of the number of arguments passed:
// If no arguments are passed to the script, print “No argument”
// If only one argument is passed to the script, print “Argument found”
// Otherwise, print “Arguments found”
// You must use console.log(...) to print all output
// You are not allowed to use var Reference: process.argv
 
function argumentsChecker() {
    
    const args = process.argv.slice(2);  // Get only the arguments excluding the first two elements
    if (args.length === 0) {
        console.log('No argument')
    }
    else if (args.length === 1) {
        console.log('Argument found');
    }
    else {
        console.log('Arguments found');
    }
}

argumentsChecker();