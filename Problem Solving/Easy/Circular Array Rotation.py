def circularArrayRotation(a, k, queries):
    for i in range(k):
        
        tmp = a[-1]
        a.pop(-1)
        a.insert(0,tmp)

    qq = []
    for q in queries:
        qq.append(a[q])
    return qq
