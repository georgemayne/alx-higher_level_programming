#!/usr/bin/node
const numArg = process.argv.length;
console.log(numArg === 2 ? 'No argument' : numArg === 3 ? 'Argument found' : 'Arguments found');
