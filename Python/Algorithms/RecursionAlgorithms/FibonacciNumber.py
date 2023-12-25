
def fibonacciNumber(n):
    """
    :return: n'th fibonacci Number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciNumber(n - 1) + fibonacciNumber(n - 2)


print(fibonacciNumber(3))
