def getMoneySpent(a,b,s):
    ans = -1
    for x in a:
        for y in b:
            if x + y <= s:
                ans = max(ans, x + y)
    return ans
