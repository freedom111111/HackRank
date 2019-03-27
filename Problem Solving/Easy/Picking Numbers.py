
def pickingNumbers(a):
    counts = Counter(a)
    ans = 0
    for i in counts.keys():
        ans = max(counts[i] + counts[i+1],ans)
    return ans
