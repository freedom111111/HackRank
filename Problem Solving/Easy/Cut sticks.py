def cutTheSticks(arr):
    woods = [len(arr)]
    arr_c = arr.copy()
    for i in range(len(set(arr_c))-1):
        min_wood = min(arr)
        arr = [(x-min_wood) for x in arr]
        arr = [x for x in arr if x !=0 ]
        woods.append(len(arr))
    return woods
