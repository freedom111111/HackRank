def kaprekarNumbers(p, q):
    res = []
    for x in range(p,q+1):
        square = x**2
        t = len(str(square))
        l = t//2
        if l == 0:
            if int(str(square)[l:]) == x:
                res.append(x)
        else:
            if (int(str(square)[:l])+int(str(square)[l:])) == x:
                res.append(x)
    if res == []:
        print('INVALID RANGE')
    else:
        res = [str(x) for x in res]
        print(' '.join(res))
