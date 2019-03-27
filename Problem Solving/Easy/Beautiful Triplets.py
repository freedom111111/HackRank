def beautifulTriplets(d, arr):
    count = 0 
    for x in arr:
        if (x+d) in arr and (x+2*d) in arr:
            count += 1
    return count
