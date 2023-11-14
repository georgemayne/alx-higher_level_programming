#!/usr/bin/node

const fs = require('fs');
const fileGem = fs.readFileSync(process.argv[2], 'utf8');
const fileMay = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], fileGem + fileMay);
