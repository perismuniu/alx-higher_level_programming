#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    const completedTasksByUser = tasks.reduce((completedCount, task) => {
      if (task.completed) {
        if (completedCount[task.userId]) {
          completedCount[task.userId]++;
        } else {
          completedCount[task.userId] = 1;
        }
      }
      return completedCount;
    }, {});

    console.log(completedTasksByUser);
  }
});
