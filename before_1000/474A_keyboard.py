letters = [''] + list('qwertyuiop') + [''] + list('asdfghjkl;') + [''] + list('zxcvbnm,./') + ['']
shift = -1 if input() == 'R' else 1
s = ''
for letter in input():
    s += letters[letters.index(letter) + shift]
print(s)