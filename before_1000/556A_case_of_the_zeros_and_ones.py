
n = int(input())
s = input()
while len(s):
    count = 0
    i = 1
    prev = s[0]
    while i < len(s):
        if s[i] != prev:
            s = s[:i-1] + s[i+1:]
            count += 1
            prev = s[i + 1] if i < len(s) - 1 else prev
            i += 2
        else:
            prev = s[i]
            i += 1
    if count == 0:
        break
print(len(s))