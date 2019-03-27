def saveThePrisoner(n, m, s):
    
    a=0
    a=(m+s-1)%n
    if a==0:
        return n
    else:
        return a
