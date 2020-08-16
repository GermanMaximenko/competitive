import threading

print(threading.active_count())  # текущее количество активных трэдов
current = threading.current_thread()
print(current.getName())
print(current.is_alive())
try:
    current.start()
except RuntimeError as e:
    print(f'ERROR {e}')  # ERROR threads can only be started once
current.setName('SuperThread')
print(current.getName())

# Set name и get name старые интерфейсы  можно так: ( на самом деле хз )
current.name = 'SuperThread1'
print(current.name)
print(current.getName())

# Вывод всех запущенных и живых трэдов

print(threading.enumerate())