def flatlandSpaceStations(n, c):
    c = sorted(c)
    maximum = max(c[0],n-1-c[-1])
    for i in range(len(c)-1):
        d = (c[i+1]-c[i])//2
        maximum = max(d,maximum)
    return maximum
