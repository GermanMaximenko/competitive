n = input()
coins = [int(el) for el in input().split()]
count_coins = 0
money_twin = 0
half_money = sum(coins)/2
while money_twin <= half_money:
    money_twin += coins.pop(coins.index(max(coins)))
    count_coins += 1
print(count_coins)


# input();a=sorted(map(int,input().split()));s=c=0
# while s<=sum(a):s+=a.pop();c+=1
# print(c)