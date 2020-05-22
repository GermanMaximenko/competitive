import random
from datetime import datetime
t1 = datetime.now()
ordered = [i for i in range(1, 100000)]
ids = [i for i in range(len(ordered))]
shuffled = [ordered[ids.pop(random.randint(0, len(ids) - 1))] for i in range(len(ordered))]
print('time 1: ', datetime.now() - t1)
t1 = datetime.now()

sorted(ordered, key=lambda a: random.randint(0, 1))
print('time 2: ', datetime.now() - t1)
