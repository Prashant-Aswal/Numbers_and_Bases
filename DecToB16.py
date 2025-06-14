def dectob16(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    val = []
    Q = int(num / 16)
    M = num % 16
    val.append(M)
    while Q > 0:
        M = Q % 16
        val.append(M)
        Q = int(Q / 16)
    val.reverse()
    t = 0
    for i in val:
        val[t] = str(val[t])
        if val[t] == '10':
            val[t] = 'A'
        elif val[t] == '11':
            val[t] = 'B'
        elif val[t] == '12':
            val[t] = 'C'
        elif val[t] == '13':
            val[t] = 'D'
        elif val[t] == '14':
            val[t] = 'E'
        elif val[t] == '15':
            val[t] = 'F'
        t = t + 1
    n = 0
    ans = None
    for i in val:
        if ans is None:
            ans = val[n]
        else:
            ans = ans + val[n]
        n = n + 1
    return ans
