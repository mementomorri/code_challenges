// Any call of sqrt_iter leads immediately to an
// infinite loop. The reason for this is our
// applicative-order evaluation. The evaluation
// of the return expression of sqrt_iter needs
// to evaluate its arguments first, including
// the recursive call of sqrt_iter, regardless
// whether the predicate evaluates to true or
// false. The same of course happens with the
// recursive call, and thus the function
// conditional never actually gets applied. 
