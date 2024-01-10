#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const val = list.filter((val) => val === searchElement);

  return val.length;
};
