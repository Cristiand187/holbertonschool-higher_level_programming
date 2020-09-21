#!/usr/bin/node
// unction that returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
  let numElement = 0;
  for (const element of list) {
    if (element === searchElement) {
      numElement += 1;
    }
  }
  return numElement;
};
