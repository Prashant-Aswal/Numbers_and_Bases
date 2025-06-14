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


def subtodec(X,B):
    try:
        X = int(X)
    except:
        return 'Invalid number'
    try:
        B = int(B)
    except:
        return 'Invalid base value'
    if B == 1:
        return 'Invalid base value'
    else:
        chk = chksub(X, B)
        if chk == 'Invalid number':
            return chk
        else:
            diff = B - 10
            N = int(X / 10)
            val = (N * diff)
            p = 1
            while N > 0:
                N = int(N / 10)
                val = val + (N * diff * (B ** p))
                p = p + 1
            ans = X + val
            return ans


def dectosub(X,B):
    try:
        X = int(X)
    except:
        return 'Invalid number'
    try:
        B = int(B)
    except:
        return 'Invalid base value'
    if B > 10 or B < 2:
        return 'Invalid base value'
    else:
        diff = 10 - B
        N = int(X / B)
        val = (N * diff)
        p = 1
        while N > 0:
            N = int(N / B)
            val = val + (N * diff * (10 ** p))
            p = p + 1
        ans = X + val
        return ans


def chk11(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a']
    for i in num:
        if i in guide:
            continue
        else:
            return 'Invalid number'
    return 'Valid'


def b11todec(num):
    num = str(num)
    chk = chk11(num)
    if chk == "Invalid number":
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


def dectob11(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    val = []
    Q = int(num / 11)
    M = num % 11
    val.append(M)
    while Q > 0:
        M = Q % 11
        val.append(M)
        Q = int(Q / 11)
    val.reverse()
    t = 0
    for i in val:
        val[t] = str(val[t])
        if val[t] == '10':
            val[t] = 'A'
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


def dectob12(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    val = []
    Q = int(num / 12)
    M = num % 12
    val.append(M)
    while Q > 0:
        M = Q % 12
        val.append(M)
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


def dectob13(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    val = []
    Q = int(num / 13)
    M = num % 13
    val.append(M)
    while Q > 0:
        M = Q % 13
        val.append(M)
        Q = int(Q / 13)
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


def chk13(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c']
    for i in num:
        if i in guide:
            continue
        else:
            return 'Invalid number'
    return 'Valid'


def b13todec(num):
    num = str(num)
    chk = chk13(num)
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
            elif val[c] == 'C' or val[c] == 'c':
                val[c] = 12
                c = c + 1
            else:
                val[c] = int(val[c])
                c = c + 1
        c = 0
        l = len(val)
        ans = 0
        for r in val:
            ans = ans + (val[c] * (13 ** (l - 1)))
            c = c + 1
            l = l - 1
        return ans


def dectob14(num):
    try:
        num = int(num)
    except:
        return 'Invalid number'
    val = []
    Q = int(num / 14)
    M = num % 14
    val.append(M)
    while Q > 0:
        M = Q % 14
        val.append(M)
        Q = int(Q / 14)
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


def chk14(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']
    for i in num:
        if i in guide:
            continue
        else:
            return 'Invalid number'
    return 'Valid'


def b14todec(num):
    num = str(num)
    chk = chk14(num)
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
            elif val[c] == 'C' or val[c] == 'c':
                val[c] = 12
                c = c + 1
            elif val[c] == 'D' or val[c] == 'd':
                val[c] = 13
                c = c + 1
            else:
                val[c] = int(val[c])
                c = c + 1
        c = 0
        l = len(val)
        ans = 0
        for r in val:
            ans = ans + (val[c] * (14 ** (l - 1)))
            c = c + 1
            l = l - 1
        return ans


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


def chk15(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e']
    for i in num:
        if i in guide:
            continue
        else:
            return 'Invalid number'
    return 'Valid'


def b15todec(num):
    num = str(num)
    chk = chk15(num)
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
            elif val[c] == 'C' or val[c] == 'c':
                val[c] = 12
                c = c + 1
            elif val[c] == 'D' or val[c] == 'd':
                val[c] = 13
                c = c + 1
            elif val[c] == 'E' or val[c] == 'e':
                val[c] = 14
                c = c + 1
            else:
                val[c] = int(val[c])
                c = c + 1
        c = 0
        l = len(val)
        ans = 0
        for r in val:
            ans = ans + (val[c] * (15 ** (l - 1)))
            c = c + 1
            l = l - 1
        return ans


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


def chk16(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']
    for i in num:
        if i in guide:
            continue
        else:
            return 'Invalid number'
    return 'Valid'


def b16todec(num):
    num = str(num)
    chk = chk16(num)
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
            elif val[c] == 'C' or val[c] == 'c':
                val[c] = 12
                c = c + 1
            elif val[c] == 'D' or val[c] == 'd':
                val[c] = 13
                c = c + 1
            elif val[c] == 'E' or val[c] == 'e':
                val[c] = 14
                c = c + 1
            elif val[c] == 'F' or val[c] == 'f':
                val[c] = 15
                c = c + 1
            else:
                val[c] = int(val[c])
                c = c + 1
        c = 0
        l = len(val)
        ans = 0
        for r in val:
            ans = ans + (val[c] * (16 ** (l - 1)))
            c = c + 1
            l = l - 1
        return ans


def base(fromB,toB,num):
    Bguide = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    Bguide1 = [2, 3, 4, 5, 6, 7, 8, 9]
    try:
        B1 = int(fromB)
        B2 = int(toB)
    except:
        return "Invalid base value"
    X = str(num)
    if B1 in Bguide and B2 in Bguide:
        if B1 == 10 and B2 in Bguide1:
            result = dectosub(X,B2)
            return result
        elif B1 in Bguide1 and B2 == 10:
            result = subtodec(X,B1)
            return result
        elif B1 == B2:
            return num
        elif B1 == 11 and B2 == 10:
            result = b11todec(X)
            return result
        elif B1 == 10 and B2 == 11:
            result = dectob11(X)
            return result
        elif B1 == 10 and B2 == 12:
            result = dectob12(X)
            return result
        elif B1 == 12 and B2 == 10:
            result = b12todec(X)
            return result
        elif B1 == 10 and B2 == 13:
            result = dectob13(X)
            return result
        elif B1 == 13 and B2 == 10:
            result = b13todec(X)
            return result
        elif B1 == 10 and B2 == 14:
            result = dectob14(X)
            return result
        elif B1 == 14 and B2 == 10:
            result = b14todec(X)
            return result
        elif B1 == 10 and B2 == 15:
            result = dectob15(X)
            return result
        elif B1 == 15 and B2 == 10:
            result = b15todec(X)
            return result
        elif B1 == 10 and B2 == 16:
            result = dectob16(X)
            return result
        elif B1 == 16 and B2 == 10:
            result = b16todec(X)
            return result
        elif B1 in Bguide1 and B2 in Bguide1:
            stage = subtodec(X,B1)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectosub(stage, B2)
                return result
        elif B1 in Bguide1 and B2 == 11:
            stage = subtodec(X,B1)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob11(stage)
                return result
        elif B1 == 11 and B2 in Bguide1:
            stage = b11todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectosub(stage, B2)
                return result
        elif B1 in Bguide1 and B2 == 12:
            stage = subtodec(X,B1)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob12(stage)
                return result
        elif B1 == 12 and B2 in Bguide1:
            stage = b12todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectosub(stage, B2)
                return result
        elif B1 in Bguide1 and B2 == 13:
            stage = subtodec(X,B1)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob13(stage)
                return result
        elif B1 == 13 and B2 in Bguide1:
            stage = b13todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectosub(stage, B2)
                return result
        elif B1 in Bguide1 and B2 == 14:
            stage = subtodec(X,B1)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob14(stage)
                return result
        elif B1 == 14 and B2 in Bguide1:
            stage = b14todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectosub(stage, B2)
                return result
        elif B1 in Bguide1 and B2 == 15:
            stage = subtodec(X,B1)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob15(stage)
                return result
        elif B1 == 15 and B2 in Bguide1:
            stage = b15todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectosub(stage, B2)
                return result
        elif B1 in Bguide1 and B2 == 16:
            stage = subtodec(X,B1)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob16(stage)
                return result
        elif B1 == 16 and B2 in Bguide1:
            stage = b16todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectosub(stage, B2)
                return result
        elif B1 == 11 and B2 == 12:
            stage = b11todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob12(stage)
                return result
        elif B1 == 11 and B2 == 13:
            stage = b11todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob13(stage)
                return result
        elif B1 == 11 and B2 == 14:
            stage = b11todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob14(stage)
                return result
        elif B1 == 11 and B2 == 15:
            stage = b11todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob15(stage)
                return result
        elif B1 == 11 and B2 == 16:
            stage = b11todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob16(stage)
                return result
        elif B1 == 12 and B2 == 11:
            stage = b12todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob11(stage)
                return result
        elif B1 == 12 and B2 == 13:
            stage = b12todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob13(stage)
                return result
        elif B1 == 12 and B2 == 14:
            stage = b12todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob14(stage)
                return result
        elif B1 == 12 and B2 == 15:
            stage = b12todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob15(stage)
                return result
        elif B1 == 12 and B2 == 16:
            stage = b12todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob16(stage)
                return result
        elif B1 == 13 and B2 == 11:
            stage = b13todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob11(stage)
                return result
        elif B1 == 13 and B2 == 12:
            stage = b13todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob12(stage)
                return result
        elif B1 == 13 and B2 == 14:
            stage = b13todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob14(stage)
                return result
        elif B1 == 13 and B2 == 15:
            stage = b13todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob15(stage)
                return result
        elif B1 == 13 and B2 == 16:
            stage = b13todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob16(stage)
                return result
        elif B1 == 14 and B2 == 11:
            stage = b14todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob11(stage)
                return result
        elif B1 == 14 and B2 == 12:
            stage = b14todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob12(stage)
                return result
        elif B1 == 14 and B2 == 13:
            stage = b14todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob13(stage)
                return result
        elif B1 == 14 and B2 == 15:
            stage = b14todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob15(stage)
                return result
        elif B1 == 14 and B2 == 16:
            stage = b14todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob16(stage)
                return result
        elif B1 == 15 and B2 == 11:
            stage = b15todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob11(stage)
                return result
        elif B1 == 15 and B2 == 12:
            stage = b15todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob12(stage)
                return result
        elif B1 == 15 and B2 == 13:
            stage = b15todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob13(stage)
                return result
        elif B1 == 15 and B2 == 14:
            stage = b15todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob14(stage)
                return result
        elif B1 == 15 and B2 == 16:
            stage = b15todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob16(stage)
                return result
        elif B1 == 16 and B2 == 11:
            stage = b16todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob11(stage)
                return result
        elif B1 == 16 and B2 == 12:
            stage = b16todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob12(stage)
                return result
        elif B1 == 16 and B2 == 13:
            stage = b16todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob13(stage)
                return result
        elif B1 == 16 and B2 == 14:
            stage = b16todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob14(stage)
                return result
        elif B1 == 16 and B2 == 15:
            stage = b16todec(X)
            if stage == 'Invalid number':
                return stage
            else:
                result = dectob15(stage)
                return result
    else:
        return "Invalid base value"
