## 최대공약수

def fi를nd_greatest_common_factor(n,m):
    if n == 0 or m == 0:
        return max(n,m)
    small_number = min(n,m)
    big_num = max(n,m)

    i = big_num
    while i > 1: #
        if big_num % i == 0 and small_number % i == 0:
            return i
        i -= 1

    return 1

print(find_greatest_common_factor(17,19))
print(find_greatest_common_factor(9,18))
print(find_greatest_common_factor(1,19))
print(find_greatest_common_factor(0,19))
print(find_greatest_common_factor(0,0))