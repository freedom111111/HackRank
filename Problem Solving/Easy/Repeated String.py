def repeatedString(s, n):
    k = s.count("a")*(n//len(s))
    k += s[:n%len(s)].count("a")
    return k
