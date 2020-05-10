# s = input()
# print(['NO', 'YES']['H' in s or 'Q' in s or '9' in s])

print(set("HQ9")&set(input())and"YES"or"NO")