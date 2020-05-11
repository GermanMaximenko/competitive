# input()
# seq = {'max': 1, 'cur': 1, 'prev_el': None}
# for el in map(int, input().split()):
#     seq['cur'] = seq['cur'] + 1 if seq['prev_el'] and el >= seq['prev_el'] else 1
#     seq['prev_el'] = el
#     if seq['cur'] > seq['max']:
#         seq['max'] = seq['cur']
# print(seq['max'])

input()
max_seq = cur_seq = prev_el = 0
for el in map(int, input().split()):
    cur_seq = cur_seq + 1 if prev_el and el >= prev_el else 1
    prev_el = el
    max_seq = max(max_seq, cur_seq)
print(max_seq)

# input()
# c=m=s=0
# for i in map(int,input().split()):
#     c=[c+1,1][i<s]
#     m=max(m,c)
#     s=i
# print(m)