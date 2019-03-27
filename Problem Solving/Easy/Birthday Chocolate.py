def birthday(s, d, m):
    res = 0
    if len(s)==m:
        return 1 if sum(s)==d else 0
    else:
        for i in range(len(s)-m+1):
            if sum(s[i:i+m])==d:
                res += 1
        return res
