#!/usr/bin/node
// script that prints the first argument passed to it:
let noarg = 'undefined'
if (process.argv[3]) {
    console.log(process.argv[2] + 'is ' + process.argv[3]);
} else if (process.argv[2]) {
    console.log(process.argv[2] + 'is ' + noarg);
} else {
    console.log(noarg + 'is ' + noarg);
}
