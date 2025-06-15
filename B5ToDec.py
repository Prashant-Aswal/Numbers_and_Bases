def chk5(num):
    i = 0
    snum = str(num)
    for n in snum:
        try:
            temp = int(n)
        except:
            return False
        if int(snum[i]) >= 5:
            return False
        else:
            i = i + 1
    return True


def b5todec(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    chk = chk5(num)
    if chk is False:
        return 'Invalid number'
    else:
        diff = 5 - 10
        N = int(num / 10)
        val = (N * diff)
        p = 1
        while N > 0:
            N = int(N / 10)
            val = val + (N * diff * (5 ** p))
            p = p + 1
        ans = num + val
        return ans
