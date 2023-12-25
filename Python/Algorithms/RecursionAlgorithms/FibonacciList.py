
def fibonacciList(n):
    """
    :return: Return Fibonacci List Upto N Number by Reursion
    """
    if n <= 1:
        return n
    else:
        return fibonacciList(n - 1) + fibonacciList(n - 2)


n = 10
fibList = [fibonacciList(i) for i in range(n)]
print(fibList)
