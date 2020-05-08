def num_participant_next_round(k, scores):
    k = int(scores[k-1])
    i = 0
    for el in scores:
        el = int(el)
        if el >= k and el != 0:
            i += 1
    return i


k = int(input().split(' ')[1])
scores = input().split(' ')
print(num_participant_next_round(k, scores))


# l=lambda:map(int,raw_input().split());n,k=l();a=l()
# print sum(v>=max(1,a[k-1])for v in a)