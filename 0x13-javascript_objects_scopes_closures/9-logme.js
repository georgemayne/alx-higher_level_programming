#!/usr/bin/node

let read = 0;
exports.logMe = function (item) { console.log(`${read++}: ${item}`); };
