from functools import reduce
n = int(input())
res = 0
for _ in range(n):
    if reduce(lambda x, y: int(x) + int(y), input().split(' ')) > 1:
        res += 1
print(res)

# print(sum(input().count('1') > 1 for x in [0] * int(input())))