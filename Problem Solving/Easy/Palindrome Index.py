def palindromeIndex(s):
    N = len(s)
    N_i = N - 1
    s_i = s[::-1]
    if s == s_i:
            return -1

    for i in range(N):
        test = s[:i] + s[i+1:]
        test_i = s_i[:N_i-i] + s_i[N_i-i+1:]
        if test == test_i:
            return i
    return -1
