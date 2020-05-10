input()
coins = sorted(map(int, input().split()))
count_coins = twin_money = 0
half_money = sum(coins)/2
while twin_money <= half_money:
    twin_money += coins.pop()
    count_coins += 1
print(count_coins)
