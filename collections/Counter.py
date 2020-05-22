from collections import Counter

# COUNTER MAY INITIALIZE LIKE THIS :
# Counter(key=val) - val must be int.
# Counter({key:val}) - val must be int.
# Counter('Abracadabra')
# Counter(['1','2','3', 3, 3, 4, '1'])


# 1. Write a Python program that iterate over elements repeating each as many times as its count.
def iterate(els):
    c = Counter(els)
    print(*list(c.elements()))


# 2. Write a Python program to find the most common elements and their counts of a specified text
def most_common(els):
    c = Counter(els)
    print(c.most_common())


elements = {'a': 3, 'b': 2, 'c': 4}
most_common(elements)
