def chksub(num,base):
    i = 0
    snum = str(num)
    try:
        base = int(base)
    except:
        return 'Invalid base value'
    if base == 1:
        return 'Invalid base value'
    else:
        for n in snum:
            try:
                temp = int(n)
            except:
                return 'Invalid number'
            if int(snum[i]) >= base:
                return 'Invalid number'
            else:
                i = i + 1
        return 'Valid'


def subtodec(X,B):
    try:
        X = int(X)
    except:
        return 'Invalid number'
    try:
        B = int(B)
    except:
        return 'Invalid base value'
    if B == 1:
        return 'Invalid base value'
    else:
        chk = chksub(X, B)
        if chk == 'Invalid number':
            return chk
        else:
            diff = B - 10
            N = int(X / 10)
            val = (N * diff)
            p = 1
            while N > 0:
                N = int(N / 10)
                val = val + (N * diff * (B ** p))
                p = p + 1
            ans = X + val
            return ans

