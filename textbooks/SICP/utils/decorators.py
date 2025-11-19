def trace_function(func):
    call_stack = []

    def wrapper(*args, **kwargs):
        call_stack.append(func.__name__)
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")

        try:
            result = func(*args, **kwargs)
            return result
        finally:
            call_stack.pop()
            print(f"Exiting {func.__name__}")

    return wrapper
