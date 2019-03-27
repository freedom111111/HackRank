 def beautifulDays(i, j, k):
    count = 0
    for n in range(i,j+1):
        num = int(str(n)[::-1])
        if abs(n-num)%k == 0:
            count+=1
            
    return count
