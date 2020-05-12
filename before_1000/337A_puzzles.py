n, m = map(int, input().split())
puzzles = sorted(map(int, input().split()))
best = float('inf')
for k in range(m - n + 1):
    best = min(best, puzzles[k + n - 1] - puzzles[k])
print(best)
