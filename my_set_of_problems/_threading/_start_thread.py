import threading
import time


def handler(started=0, finished=0):
    sum = 0
    for i in range(started, finished):
        sum += i
    print('Result:', sum)


params = {'finished': 2 ** 26}
t1 = threading.Thread(target=handler, kwargs=params)

print('Started by thread')
start = time.time()
t1.start()
t1.join()
print(f'Execute time = {time.time() - start}')

start = time.time()
print('Started by Main thread')
handler(**params)
print(f'Execute time = {time.time() - start}')
