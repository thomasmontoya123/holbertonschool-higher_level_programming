#!/usr/bin/node
exports.esrever = function (list) {
  var newArray = [];
  for (var i = list.length - 1; i >= 0; i--) {
    newArray.push(list[i]);
  }
  return newArray;
};
