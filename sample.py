fib = lambda n: 1 if n in (0, 1) else fib(n - 1) + fib(n - 2)


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)
