def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    k = 0
    if s<p:
        return 0
    else:
        while p>m and s>0:
            s -= p
            p -= d
            k += 1
        k += s//m
        return k  
