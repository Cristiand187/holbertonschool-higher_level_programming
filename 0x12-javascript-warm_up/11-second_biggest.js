#!/usr/bin/node
// cript that searches the second biggest integer in the list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arrNums = process.argv.slice(2).sort((a, b) => a - b);
  console.log(arrNums[arrNums.length - 2]);
}
