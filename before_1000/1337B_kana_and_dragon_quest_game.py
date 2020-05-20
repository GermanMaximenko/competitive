for i in range(int(input())):
    x, n, m = map(int, input().split())
    while m and x > 0:
        if x > 20 and n:
            x = x//2 + 10
            n -= 1
        else:
            x = x - 10
            m -= 1
    print(['YES', 'NO'][x > 0])
