from typing import Callable


def iterative_improve(good_enough: Callable, improve: Callable) -> Callable:
    """Write a function iterative_improve that takes two functions as
    arguments:
    - a method for telling whether a guess is good enough
    - and a method for improving a guess.
    The function iterative_improve should return as its value a function that takes
    a guess as argument and keeps improving the guess until it is good enough."""

    def iterate(guess):
        return guess if good_enough(guess) else iterate(improve(guess))

    return iterate
