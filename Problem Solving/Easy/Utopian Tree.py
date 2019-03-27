def utopianTree(n):
    if n%2 == 1:
        return int(2**((n+1)/2+1)-2)
    else:
        return int(2**(n/2+1)-1)
