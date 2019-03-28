def strangeCounter(t):
    rem = 3
    while t>rem:
        t -= rem
        rem *= 2
    return rem-t+1
