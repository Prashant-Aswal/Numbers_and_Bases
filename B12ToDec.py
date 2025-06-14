def chk12(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b']
    for i in num:
        if i in guide:
            continue
        else:
            return 'Invalid number'
    return 'Valid'


def b12todec(num):
    num = str(num)
    chk = chk12(num)
    if chk == 'Invalid number':
        return chk
    else:
        val = []
        c = 0
        for n in num:
            val.append(num[c])
            c = c + 1
        c = 0
        for p in val:
            if val[c] == 'A' or val[c] == 'a':
                val[c] = 10
                c = c + 1
            elif val[c] == 'B' or val[c] == 'b':
                val[c] = 11
                c = c + 1
            else:
                val[c] = int(val[c])
                c = c + 1
        c = 0
        l = len(val)
        ans = 0
        for r in val:
            ans = ans + (val[c] * (12 ** (l - 1)))
            c = c + 1
            l = l - 1
        return ans
