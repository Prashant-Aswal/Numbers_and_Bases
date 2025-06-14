def chksub(num,base):
    i = 0
    snum = str(num)
    try:
        base = int(base)
    except:
        return 'Invalid base value'
    if base == 1:
        return 'Invalid base value'
    else:
        for n in snum:
            try:
                temp = int(n)
            except:
                return 'Invalid number'
            if int(snum[i]) >= base:
                return 'Invalid number'
            else:
                i = i + 1
        return 'Valid'
