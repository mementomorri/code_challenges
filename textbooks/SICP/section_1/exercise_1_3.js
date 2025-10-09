// exercise 1.3
function three_sum(a, b, c){
  return a >= c && b >= c ? a**2 + b**2 
    : a >= b && c >= b ? a**2 + c**2
      : b >= a && c >= a ? b**2 + c**2
        :0;
}

console.log(three_sum(1, 2, 3))  // 13
console.log(three_sum(3, 2, 1))  // 13
console.log(three_sum(3, 1, 2))  // 13
console.log(three_sum(2, 2, 2))  // 8
console.log(three_sum(1, 2, 1))  // 5
