def workbook(n, k, arr):
    cnt = 0 # special problems
    i = 0   # chapter number
    j = 1   # page number
    m = 1   # problem number

    while i<n:
        if j>=m and j<=min(m+k-1,arr[i]):
            cnt += 1
        j += 1
        m += k
        if m>arr[i]:
            i += 1
            m=1
    return cnt
