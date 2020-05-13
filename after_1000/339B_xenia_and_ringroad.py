n, m = map(int, input().split())
summ = 0
prev = 1
for el in map(int, input().split()):
    summ += el - prev if el >= prev else n - prev + el
    prev = el
print(summ)