def serviceLane(width, cases):
    ll = []
    for x in cases:
        start,end = x
        ll.append(min(width[start:end+1]))
    return ll
