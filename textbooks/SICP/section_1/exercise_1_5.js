function p() { return p(); }

function test(x, y) {
    return x === 0 ? 0 : y;
}

console.log(test(0, p()));  // infinite recursion

// solution quote
// In applicative-order evaluation of test(0, p()), 
// we need to evaluate the argument expressions before 
// we can evaluate the return expression of the function test. 
// The evaluation of the argument expression p() will not terminate, 
// however: It will keep evaluating application expressions 
// of the form p(), and thus the evaluation of test(0, p()) will not 
// produce a legitimate value. In normal-order evaluation, 
// on the other hand, the function application test(0, p()) would 
// immediately evaluate the return expression of the function test, 
// x === 0 ? 0 : y after replacing the parameter x with 0 and y with p(). 
// The result of the replacing would be 0 === 0 ? 0 : p(). 
// The evaluation of the predicate 0 === 0 results in true and 
// thus the conditional expression evaluates to 0, without any 
// need to evaluate p(). 
