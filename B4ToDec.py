def chk4(num):
    i = 0
    snum = str(num)
    for n in snum:
        try:
            temp = int(n)
        except:
            return False
        if int(snum[i]) >= 4:
            return False
        else:
            i = i + 1
    return True


def b4todec(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    chk = chk4(num)
    if chk is False:
        return 'Invalid number'
    else:
        diff = 4 - 10
        N = int(num / 10)
        val = (N * diff)
        p = 1
        while N > 0:
            N = int(N / 10)
            val = val + (N * diff * (4 ** p))
            p = p + 1
        ans = num + val
        return ans
