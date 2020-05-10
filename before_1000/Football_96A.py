# prev = None
# output = 'NO'
# count = 1
# for el in input():
#     count = count + 1 if prev and prev == el else 1
#     prev = el
#     if count == 7:
#         output = 'YES'
#         break
# print(output)

s=input();print(["NO","YES"][7*"1"in s or 7*"0"in s])