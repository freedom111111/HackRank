def countingValleys(n, s):
    land = 0
    cnt = 0
    for i in range(n):
        if s[i]=='U':
            land += 1 
        if s[i]=='D':
            land -= 1
        if land == 0 and s[i]=='U':
            cnt += 1
    return cnt
