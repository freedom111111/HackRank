def pageCount(n, p):
    start = p//2
    end = n//2-p//2
    return start if start<=end else end
