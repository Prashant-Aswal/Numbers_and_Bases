def chksub(num, base):
    i = 0
    snum = str(num)
    try:
        base = int(base)
    except:
        return 'Invalid base value'
    if base < 2 or base > 10:
        return 'Invalid base value'
    else:
        for n in snum:
            try:
                temp = int(n)
            except:
                return False
            if int(snum[i]) >= base:
                return False
            else:
                i = i + 1
        return True


def subtodec(num, fromB):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    try:
        fromB = int(fromB)
    except:
        return 'Invalid base value'
    if fromB < 2 or fromB > 10:
        return 'Invalid base value'
    else:
        chk = chksub(num, fromB)
        if chk is False:
            return 'Invalid number'
        elif chk == 'Invalid base value':
            return chk
        else:
            diff = fromB - 10
            N = int(num / 10)
            val = (N * diff)
            p = 1
            while N > 0:
                N = int(N / 10)
                val = val + (N * diff * (fromB ** p))
                p = p + 1
            ans = num + val
            return ans
