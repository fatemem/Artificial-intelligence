include "alldifferent.mzn";
var {3}: x1;
var {2,3}: x2;
var {1,2,3}: x3;
var {1,2,3}: x4;
var {2,3}: x5;

constraint x2!=x4;
constraint x4!=x3;
constraint x4!=x5;
constraint x5!=x3;
constraint x2!=3;
constraint x3!=2;
solve satisfy;