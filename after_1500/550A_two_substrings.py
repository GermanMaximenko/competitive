s = input()
prev = s[0]
cond = False
for i in range(1, len(s)):
    if prev + s[i] == 'AB':
        cond = 'BA' in s[0:i-1] + '  ' + s[i+1:len(s)]
    elif prev + s[i] == 'BA':
        cond = 'AB' in s[0:i-1] + '  ' + s[i+1:len(s)]
    prev = s[i]
    if cond:
        break
print(['NO', 'YES'][cond])

# s=input()
# u=s.find('AB');v=s.find('BA')
# print('YES'if (u+1 and s.find('BA',u+2)+1) or (v+1 and s.find('AB',v+2)+1)else'NO')