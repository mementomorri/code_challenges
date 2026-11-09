def plus_curried(x):
    return lambda y: x + y


def brooks(f, args):
    current_result = f
    for arg in args:
        current_result = current_result(arg)
    return current_result


def brooks_curried(items):
    return brooks(items[0], items[1:])


def run_tests():
    print("Running tests...")

    try:
        print("Test 1: plus_curried(3)(4) == 7", end="... ")
        assert plus_curried(3)(4) == 7
        print("PASSED")

        print("Test 2: brooks(plus_curried, [3, 4]) == 7", end="... ")
        assert brooks(plus_curried, [3, 4]) == 7
        print("PASSED")

        print("Test 3: brooks_curried([plus_curried, 3, 4]) == 7", end="... ")
        assert brooks_curried([plus_curried, 3, 4]) == 7
        print("PASSED")

        print("Test 4: Nested Puzzle Level 1 == 7", end="... ")
        res1 = brooks_curried([brooks_curried, [plus_curried, 3, 4]])
        assert res1 == 7
        print("PASSED")

        print("Test 5: Nested Puzzle Level 2 == 7", end="... ")
        res2 = brooks_curried([brooks_curried, [brooks_curried, [plus_curried, 3, 4]]])
        assert res2 == 7
        print("PASSED")

        print("\nAll tests passed successfully!")

    except AssertionError as e:
        print("FAILED")
        print(f"Assertion Error: {e}")
    except Exception as e:
        print("FAILED")
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    run_tests()
