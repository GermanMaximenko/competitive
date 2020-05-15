n, m = map(int, input().split())
summ = n
while n // m > 0:
    summ += n // m
    n = n // m + n % m
print(summ)