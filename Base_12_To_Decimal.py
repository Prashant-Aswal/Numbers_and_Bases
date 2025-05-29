def check(num,guide):
    t = 0
    for i in num:
        if (num[t] in guide) is True:
            t = t + 1
        else:
            t = 'Invalid'
            break
    if t == 'Invalid':
        return t
    else:
        return 'Valid'


def b12todec(num):
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


guide_one = ['0','1','2','3','4','5','6','7','8','9','A','B','a','b']
guide = ['0','1','2','3','4','5','6','7','8','9','A','B']
while True:
    print('\n')
    print('Use this guide for Base-12 Integers:')
    print('\n')
    print(guide)
    print('\n')
    print('This guide is not case sensitive i.e 34A and 34a will be treated alike')
    print('\n')
    num = input('Enter the Base-12 Integer(following the guide): ')
    x = check(num,guide_one)
    if x == 'Invalid':
        print('Entered Number does not follow the guide')
        continue
    elif x == 'Valid':
        break
result = b12todec(num)
print('\n')
print(num,'in Decimal is:',result)
print('\n')