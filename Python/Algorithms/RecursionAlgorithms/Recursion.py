
def recusiveSum(number):
    # Base Case
    if number == 1:
        return 1
    else:
        return number + recusiveSum(number - 1)


print(recusiveSum(5))
