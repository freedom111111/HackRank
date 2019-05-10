n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def beautiful_pair(a,b):
    common_num = set(a).intersection(set(b))
    res = 0
    for n in common_num:
        if a.count(n)<=b.count(n):
            for _ in range(a.count(n)):
                res += 1
                a.remove(n)
        else:
            for _ in range(b.count(n)):
                res += 1
                a.remove(n)
    if a:
        res += 1
    else:
        res -= 1

#    print(a)
    return res
print(beautiful_pair(a,b))
