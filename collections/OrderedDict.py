from collections import OrderedDict, Counter

# 5. Write a Python program that accept some words and count the number of distinct words.
# Print the number of distinct words and number of occurrences for each distinct word according to their appearance


class OrderedCounter(Counter, OrderedDict):
    pass


word_array = []
n = int(input('input number of words, then the words\n'))
for i in range(n):
    word_array.append(input().strip())
word_ctr = OrderedCounter(word_array)
print(len(word_ctr))
for word in word_ctr:
    print(word_ctr[word], end=' ')

# разобратьс в коде и ordered dict