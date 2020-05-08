# def words_converter(word):
#     return word[0] + str(len(word) - 2) + word[-1] if len(word) > 10 else word
#
#
# lines = int(input())
# arr = []
# for i in range(lines):
#     arr.append(input())
#
# for el in arr:
#     print(words_converter(el))

i = input

for _ in [0] * int(i()):
    s = i()
    l = len(s) - 2
    print([s, s[0] + str(l) + s[-1]][l > 8])