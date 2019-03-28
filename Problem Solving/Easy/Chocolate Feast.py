def chocolateFeast(n, c, m):
    total = n//c
    wrappers = total
        
    while wrappers >= m:
        wrappers += 1 - m
        total += 1
        
    return total
