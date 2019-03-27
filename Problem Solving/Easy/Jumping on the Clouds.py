def jumpingOnClouds(c, k):
    i = 0
    n = len(c)
    e = 100
    while i+k<n:
        if c[(i+k)%n] == 1:
            e -= 3
        else:
            e -= 1
        i = (i+k)%n
        print(i,e)
    return e-1 if c[0]==0 else e-3
