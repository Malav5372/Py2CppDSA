
def factors(n, i):
    if i <= n:
        if n % i == 0:
            print(i, end="|")
        factors(n, i + 1)


if __name__ == "__main__":
    factors(10, 1)
