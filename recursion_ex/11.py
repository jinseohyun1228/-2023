def pibo(n):
    if n < 2:
        return n
    return pibo(n - 1) + pibo(n - 2)


print(pibo(int(input())))