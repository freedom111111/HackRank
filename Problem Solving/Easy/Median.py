def findMedian(arr):
    arr = sorted(arr)
    n = len(arr)
    median = (arr[n//2]+arr[n-1-n//2])/2
    return int(median)
