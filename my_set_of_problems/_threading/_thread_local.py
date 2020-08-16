# Потокобезопасное хранилище
# Если в рамках одного потока присвоили значение
# То оно не будет пересекаться со значениями в рамках других потоков

import threading

thread_data = threading.local()
thread_data.value = 5


def print_res():
    print(threading.current_thread())
    print(f'Result: {thread_data.value}')


def count(started, to_value):
    print(hasattr(thread_data, 'value'))
    thread_data.value = started
    for i in range(to_value):
        thread_data.value += 1
    print_res()


task1 = threading.Thread(target=count, args=(0, 10), name='Thread1')
task2 = threading.Thread(target=count, args=(10, 20), name='Thread2')

task1.start()
task2.start()
task1.join()
task2.join()

print_res()