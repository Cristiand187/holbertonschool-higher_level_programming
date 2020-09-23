#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const completed = {};
    const tasks = JSON.parse(response.body);
    for (const item of tasks) {
      if (item.completed === true) {
        if (completed[item.userId] === undefined) {
          completed[item.userId] = 1;
        } else {
          completed[item.userId] += 1;
        }
      }
    }
    console.log(completed);
  }
});
