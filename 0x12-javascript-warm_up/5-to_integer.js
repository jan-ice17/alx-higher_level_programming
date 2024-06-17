#!/usr/bin/node

const firstAgrs = process.argv[2];
const num = Number(firstAgrs);

if (Number.isInteger(num)) {
    console.log(`My number: ${num}`);
}
else {
    console.log('Not a number');
}
