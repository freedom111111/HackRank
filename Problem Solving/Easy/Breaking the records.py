#!bin/bash/python3

def breakrecords(a):

    best_record = a[0]
    worst_record = a[0]

    better = 0
    worse = 0 
    
    for x in a:
        if x >best_record:
            better +=1
            best_record = x
        elif x <worst_record:
            worse +=1
            worst_record = x
    
    return better, worse
