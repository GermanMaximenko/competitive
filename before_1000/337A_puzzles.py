n, m = map(int, input().split())
puzzles = list(map(int, input().split()))
average = sum(puzzles)/m
min_diff = min_id = 0
buff = []
while n:
    min_diff = 0
    for i in range(len(puzzles)):
        if abs(puzzles[i]-average) < min_diff or not min_diff:
            min_diff = abs(puzzles[i]-average)
            min_id = i
    buff.append(puzzles.pop(min_id))
    n = n-1
print(max(buff)-min(buff))
