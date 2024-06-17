#!/usr/bin/node

function largestint() {
    
    const args = process.argv.slice(2).map(Number);

    if (args.length <= 2) {
        console.log('0')
    }
    else if (args.length == 3) {
        console.log('0');
    }
    else {
        console.log('0');
    }
}

largestint();