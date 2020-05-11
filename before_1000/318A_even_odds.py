n, k = map(int, input().split())
print([2*(k-(n-n//2)), 2*k-1][k<=n-n//2])

# from datetime import datetime
#
#
# def seq(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 2
#     count = 2
#     while count <= n:
#         yield count
#         count += 2
#
#
# t1 = datetime.now()
# n, k = map(int, input().split())
# nums = seq(n)
# for i in range(k-1):
#     next(nums)
# print(next(nums))
# print(datetime.now() - t1)

# n, k = map(int, input().split())
# count_odds = n - n//2
# if k > count_odds:
#     print(2 * (k - count_odds))
# else:
#     print(2 * k - 1)
