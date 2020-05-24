from collections import deque

# 3. Write a Python program to create a new deque with three items and iterate over the deque's elements

deq = deque()  # <---- iterable or nothing
deq.append(1)
deq.appendleft(2)
deq.append(3)

for el in deq:
    print(el)  # 2 1 3

deq = deque('abracadabra')
for el in deq:
    print(el)  # a b r a c a d a b r a