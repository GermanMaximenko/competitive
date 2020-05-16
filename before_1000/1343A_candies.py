#
# n = int(input())
# for i in range(n):
#     num = int(input())
#     x = 1
#     while True:
#         count = res = 0
#         while res < num:
#             res += x * 2**count
#             count += 1
#         if res == num:
#             print(x)
#             break
#         else:
#             x += 1
#

for i in range(int(input())):
    num = int(input())
    count = 2
    divisor = 3
    while num % divisor:
        divisor += 2**count
        count += 1
    print(num // divisor)

# for s in [*open(0)][1:]:
#     n, k = int(s), 3
#     while n % k:
#         k -= ~k
#     print(n//k)

