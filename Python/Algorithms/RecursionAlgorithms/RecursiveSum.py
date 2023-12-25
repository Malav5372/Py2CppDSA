
def recursiveSum(arr: list):
    """
    input : List
    output : Return Recursive Sum
    >>> print(recursiveSum([6,4,2]))
    """
    if arr == []:
        return 0
    else:
        head = arr[0]
        smallerList = arr[1:]
        return head + recursiveSum(smallerList)
