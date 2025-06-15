def dectob6(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    diff = 10 - 6
    N = int(num / 6)
    val = (N * diff)
    p = 1
    while N > 0:
        N = int(N / 6)
        val = val + (N * diff * (10 ** p))
        p = p + 1
    ans = num + val
    return ans
