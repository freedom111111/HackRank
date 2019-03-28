def stones(n, a, b):
            
    return sorted(set([i*a+(n-1-i)*b for i in range(n)]))
