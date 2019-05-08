n = int(input())
arr = list(map(int, input().rstrip().split()))
## qucik sort array O(nlogn)

def closest_numbers(arr):
    arr = sorted(arr)
    min_diff = arr[1]-arr[0]
    res = [arr[0],arr[1]]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]<min_diff:
            res = []
            res += [arr[i-1],arr[i]]
            min_diff = arr[i]-arr[i-1]
        elif arr[i]-arr[i-1] ==min_diff:
            res += [arr[i-1],arr[i]]
    
    return res
print(*closest_numbers(arr))
