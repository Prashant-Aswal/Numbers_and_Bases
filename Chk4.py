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
