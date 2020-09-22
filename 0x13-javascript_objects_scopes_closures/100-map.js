#!/usr/bin/node
// script that imports an array and computes a new array
let n = require('./100-data').list;
console.log(n);
console.log(n.map((x, y) => x * y));
