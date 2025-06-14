def dectob15(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    val = []
    Q = int(num / 15)
    M = num % 15
    val.append(M)
    while Q > 0:
        M = Q % 15
        val.append(M)
        Q = int(Q / 15)
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
