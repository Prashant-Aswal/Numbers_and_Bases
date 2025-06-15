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
