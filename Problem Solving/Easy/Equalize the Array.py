def equalizeArray(arr):
    max_count = 0
    for x in set(arr):
        count = arr.count(x)
        if count >= max_count:
            max_count = count
    
    return len(arr)-max_count
