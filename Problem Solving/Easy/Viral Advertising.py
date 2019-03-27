def viralAdvertising(n):
    count = 0
    share = 5
    cumulative = 0
    for i in range(n):
        like = int(share/2)
        share = like *3
        cumulative += like
        
    return cumulative
