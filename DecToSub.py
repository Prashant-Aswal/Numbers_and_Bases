def dectosub(X,B):
    try:
        X = int(X)
    except:
        return 'Invalid number'
    try:
        B = int(B)
    except:
        return 'Invalid base value'
    if B > 10 or B < 2:
        return 'Invalid base value'
    else:
        diff = 10 - B
        N = int(X / B)
        val = (N * diff)
        p = 1
        while N > 0:
            N = int(N / B)
            val = val + (N * diff * (10 ** p))
            p = p + 1
        ans = X + val
        return ans

