## remember for this question list.index don't work
n, k = map(int, input().split())
p = list(map(lambda s: int(s) - 1, input().split()))

where = [-1] * n
for i, x in enumerate(p):
    where[x] = i

for i in range(n):
    if k == 0:
        break
    if p[i] != n - 1 - i:
        bad_pos = where[n - 1 - i]
        bad_num = p[i]
        p[i], p[bad_pos] = p[bad_pos], p[i]
        where[bad_num], where[n - 1 - i] = where[n - 1 - i], where[bad_num]
        k -= 1
    
print(' '.join(map(lambda x: str(x + 1), p)))
