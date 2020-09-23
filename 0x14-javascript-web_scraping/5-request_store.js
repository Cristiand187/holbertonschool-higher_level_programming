#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, response.body, 'utf-8');
  }
});
