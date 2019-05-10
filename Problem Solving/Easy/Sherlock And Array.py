# Complete the balancedSums function below.
def balancedSums(arr):
    summy = sum(arr)
    left = 0
    for i in range(len(arr)):
        summy -= arr[i]
        if summy == left:
            return 'YES'
        left += arr[i]
    return 'NO'
