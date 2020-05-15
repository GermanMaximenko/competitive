n = int(input())
for i in range(n):
    num = int(input())
    x = 1
    while True:
        count = res = 0
        while res < num:
            res += x * 2**count
            count += 1
        if res == num:
            print(x)
            break
        else:
            x += 1
