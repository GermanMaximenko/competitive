import threading
import time


def producer(product):
    time.sleep(5)
    print('Product found')
    product.set()  # событие произошло
    product.clear()  # очищаем информацию о том что событие произошло


def consumer(product):
    print('Product wait')
    product.wait()
    print('Product exists')


event = threading.Event()

t1 = threading.Thread(target=consumer, args=(event,))
t2 = threading.Thread(target=producer, args=(event,))

t1.start()
t2.start()

t1.join()
t2.join()
