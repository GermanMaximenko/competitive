x = 0
for _ in [0]*int(input()):
    x = x + 1 if '+' in input() else x - 1
print(x)

# print(sum(44-ord(input()[1])for i in[0]*int(input())))