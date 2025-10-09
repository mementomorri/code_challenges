// exercise 1.1.7

function abs(x) {
    return x >= 0 ? x : - x;
}

function square(x) {
    return x * x;
}

function is_good_enough(guess, x, p_guess) {
    return p_guess === 0 
    ? abs(square(guess) - x) < 0.001
    : abs(p_guess - guess) < 0.001;
}

function average(x, y) {
    return (x + y) / 2;
}

function improve(guess, x) {
    return average(guess, x / guess);
}

function sqrt_iter(guess, x, p_guess=0) {
    return is_good_enough(guess, x, p_guess)
           ? guess
           : sqrt_iter(improve(guess, x), x, guess);
}


console.log(sqrt_iter(3, 0.0001));

console.log(sqrt_iter(3, 25));

