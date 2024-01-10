def factori(n):
    if(n==0):
        return 1
    return n * factori(n-1)

#print(factori(10))

x = int(input())
print(factori(x))