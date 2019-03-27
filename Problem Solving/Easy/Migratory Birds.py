def migratoryBirds(arr):
    count_dict = {x:arr.count(x) for x in set(arr)}
    count = sorted(count_dict, key=count_dict.get, reverse=True)    
    return count[0]
