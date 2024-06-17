#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const firstAgrs = process.argv[2];
const secArgs = process.argv[3];

const num1 = Number(firstAgrs);
const num2 = Number(secArgs);

if (Number.isInteger(num1) && (Number.isInteger(num2))) {
    const addResult = add(num1, num2);
    console.log(addResult);
}
else {
    console.log(num1);
}
