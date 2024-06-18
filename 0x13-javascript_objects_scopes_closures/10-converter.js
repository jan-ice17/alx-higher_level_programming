#!/usr/bin/node

// Write a function that converts a number from base 10 to another base passed as arg

exports.converter = function (base) {
    return function (number) {
      return number.toString(base);
    };
  };