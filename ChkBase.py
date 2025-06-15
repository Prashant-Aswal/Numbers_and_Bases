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


def chk11(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True


def chk12(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True


def chk13(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True


def chk14(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True


def chk15(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True


def chk16(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True


def chkbase(num, base):
    try:
        base = int(base)
    except:
        return 'Invalid base value'
    if base < 2 or base > 16:
        return 'Invalid base value'
    else:
        Bguide = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        num = str(num)
        if base in Bguide:
            result = chksub(num,base)
            return result
        elif base == 11:
            result = chk11(num)
            return result
        elif base == 12:
            result = chk12(num)
            return result
        elif base == 13:
            result = chk13(num)
            return result
        elif base == 14:
            result = chk14(num)
            return result
        elif base == 15:
            result = chk15(num)
            return result
        elif base == 16:
            result = chk16(num)
            return result
