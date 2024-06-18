#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const diction = require('./101-data').dict;
const newDicty= {};

Object.keys(diction).map(function (key, index) {
  if (y[diction[key]] === undefined) {
    newDicty[diction[key]] = [];
  }
  newDicty[diction[key]].push(key);
});

console.log(newDicty)