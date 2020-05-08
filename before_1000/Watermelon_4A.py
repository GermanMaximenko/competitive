# w = int(input())
# if w % 2 == 0 and w != 2:
#     print('YES')
# else:
#     print('NO')
from datetime import datetime
t1 = datetime.now()
print("YNEOS"[2**int(input())%24<9::2])
print('Время выполнения: ' + str(datetime.now() - t1))
