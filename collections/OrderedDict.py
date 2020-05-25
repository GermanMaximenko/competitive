from collections import OrderedDict, Counter

# 5. Write a Python program that accept some words and count the number of distinct words.
# Print the number of distinct words and number of occurrences for each distinct word according to their appearance

#
# class OrderedCounter(Counter, OrderedDict):
#     pass
#
#
# word_array = []
# n = int(input('input number of words, then the words\n'))
# for i in range(n):
#     word_array.append(input().strip())
# word_ctr = OrderedCounter(word_array)
# print(len(word_ctr))
# for word in word_ctr:
#     print(word_ctr[word], end=' ')

# 6. Write a Python program that accept name of given subject and marks.
# Input number of subjects in first line and subject name,marks separated by a space in next line.
# Print subject name and marks in order of its first occurrence

# debug this
import collections
import  re

n = int(input("Number of subjects: "))
item_order = collections.OrderedDict()
for i in range(n):
    sub_marks_list = re.split(r'(\d+)$', input("Input Subject name and marks: ").strip())
    subject_name = sub_marks_list[0]
    item_price = int(sub_marks_list[1])
    if subject_name not in item_order:
        item_order[subject_name] = item_price
    else:
        item_order[subject_name] = item_order[subject_name] + item_price

for i in item_order:
    print(i + str(item_order[i]))