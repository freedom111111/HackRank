def angryProfessor(k, a):
    arrive = [1 if x<=0 else 0 for x in a]
    total = sum(arrive)
    if total >=k:
        return 'NO'
    else:
        return 'YES'
