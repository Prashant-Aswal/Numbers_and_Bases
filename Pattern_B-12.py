def dectob12(num):
    val = []
    Q = int(num / 12)
    R = num % 12
    val.append(R)
    while Q > 0:
        R = Q % 12
        val.append(R)
        Q = int(Q / 12)
    val.reverse()
    t = 0
    for i in val:
        val[t] = str(val[t])
        if val[t] == '10':
            val[t] = 'A'
        elif val[t] == '11':
            val[t] = 'B'
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


# CREATING A TABLE OF 12
n = 1
tab = []
while n <= (12 ** 4):
    tab.append(n * 12)
    n = n + 1


# CHECKING FOR THE FORMULA
to_add = 0
n = 1
t = 0
for i in tab:
    cal = i - ((2 * n) + to_add)
    res = dectob12(i)
    try:
        res = int(res)
        if cal == res:
            print('Diff of 2n +',to_add,'works for',n)
            n = n + 1
            t = t + 1
        else:
            print('no match')
            break
    except:
        print('Result contains characters for:', n)
        to_add = to_add + 10
        n = n + 1
        t = t + 1
        continue
print('Number of Loop Runs:',t)