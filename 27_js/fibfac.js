//Team TJMax :: Jessica Yu, Tracy Ye
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>

function fact(n){
    if(n == 1){
      return 1;
    }
      return (n*fact(n-1));
  }

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

fact(1) = 1
fact(2) = 2
fact(3) = 6
fact(4) = 24
fact(5) = 120
fact(6) = 720
fact(7) = 5040
fact(8) = 40320

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

function fib(n){
    if(n == 0){
      return 0;
    }
      if(n == 1){
      return 1;
    }
    return fib(n-1)+fib(n-2);
  } 

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(7) = 13
fib(8) = 21

//=================================================================
