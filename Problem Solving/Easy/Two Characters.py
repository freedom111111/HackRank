n = int(input())
s = str(input())

from itertools import combinations
def make_arr(s,a,b):
    res = []
    for x in s:
        if x==a or x==b:
            res.append(x)
    return ''.join(res)

def check(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return False
    return True

ans = 0
for com in combinations(set(s),2):
    l = make_arr(s,com[0],com[1]) 
    if check(l):
        ans = max(ans,len(l))
print(ans)




