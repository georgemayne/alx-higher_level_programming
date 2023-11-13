#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let g = 0; g < x; g++) theFunction();
};
