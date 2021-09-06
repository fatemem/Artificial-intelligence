% Use this editor as a MiniZinc scratch book
var {9,3}:x4;



var {6,7,8}:x3;



var {3,5}:x2;




var {21,31}:x1;




constraint if x2 == 3 then  x4 != 9 else true endif ;

constraint if x1 == 31 then  x2 != 4 else true endif ;

constraint if x1 == 31 then  x4 != 9 else true endif ;

constraint if x1 == 31 then  x3 != 7 else true endif ;

constraint if x1 == 21 then  x3 != 7 else true endif ;


solve satisfy;


