n = int(input())
numbers = list(map(int,input().split()))
#print(numbers)

def counting_sort(arr):
    max_num = max(arr)+1
    counts = [0]*max_num
    for _ in arr:
        counts[_] += 1
    res = []
    for i in range(max_num):
        for j in range(counts[i]):
            res.append(i)
    return ' '.join(map(str,res))
    
print(counting_sort(numbers))
