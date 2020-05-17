from string import ascii_lowercase
from math import ceil
for _ in range(int(input())):
    n, a, b, = map(int, input().split())
    letters = ascii_lowercase[:b]
    print((letters * ceil(n/b))[:n])

# print(''.join(chr(97+i%b)for i in range(n)))
