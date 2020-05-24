from collections import Counter
from string import ascii_letters
import re

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
def most_common(els, count=None):
    c = Counter(els)
    return c.most_common(count)

# elements = {'a': 3, 'b': 2, 'c': 4}


# 4. Write a Python program to find the occurrences of 10 most common words in a given text
def del_non_letter_from_word(s):
    return ''.join([el for el in s if el in ascii_letters])

text = """
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them?
To die: to sleep;
No more; and, by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause.
"""

# print(most_common([del_non_letter_from_word(el) for el in text.lower().split()]))
print(most_common(re.findall('\w+', text)))
