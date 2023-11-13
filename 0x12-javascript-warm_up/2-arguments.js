#!/usr/bin/node
const countArg = process.argv.length;
console.log(countArg === 2 ? 'No argument' : countArg === 3 ? 'Argument found' : 'Arguments found');
