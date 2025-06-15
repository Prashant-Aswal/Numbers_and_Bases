def dectosub(num, toB):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    try:
        toB = int(toB)
    except:
        return 'Invalid base value'
    if toB > 10 or toB < 2:
        return 'Invalid base value'
    else:
        diff = 10 - toB
        N = int(num / toB)
        val = (N * diff)
        p = 1
        while N > 0:
            N = int(N / toB)
            val = val + (N * diff * (10 ** p))
            p = p + 1
        ans = num + val
        return ans
