def minimumDistances(a):
    if len(set(a)) == len(a):
        return -1
    else:
        dis = []
        ll = [x for x in a if a.count(x)==2]
        for x in set(ll):
            ind = [i for i,k in enumerate(a) if k==x]
            dis.append(abs(ind[0]-ind[1]))
            #print(dis)
        return min(dis)
