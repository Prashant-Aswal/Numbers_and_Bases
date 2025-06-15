def chk11(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True


def b11todec(num):
    num = str(num)
    chk = chk11(num)
    if chk is False:
        return 'Invalid number'
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
            else:
                val[c] = int(val[c])
                c = c + 1
        c = 0
        l = len(val)
        ans = 0
        for r in val:
            ans = ans + (val[c] * (11 ** (l - 1)))
            c = c + 1
            l = l - 1
        return ans
