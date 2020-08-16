import threading
import time


def handler(results, started=0, finished=0):
    sum = 0
    for i in range(started, finished):
        sum += i
    results.append(sum)


results = []

params = {'finished': 2 ** 26}
t1 = threading.Thread(target=handler, args=[results], kwargs={'finished': 2**25})
t2 = threading.Thread(target=handler, args=[results], kwargs={'started': 2**25, 'finished': 2**26})

print('Started by thread')
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()

print(f'Execute time = {time.time() - start}')
print(f'Result: {sum(results)}')

results = []
start = time.time()
print('Started by Main thread')
handler(results, **params)
print(f'Execute time = {time.time() - start}')
print(f'Result: {sum(results)}')

