def dectoanyb(num,base):
    val = []
    Q = num / base
    M = num % base
    Q = int(Q)
    val.append(M)
    while Q > 0:
        M = Q % base
        val.append(M)
        Q = Q / base
        Q = int(Q)
    val.reverse()
    l = len(val)
    ans = 0
    for x in val:
        ans = ans + (x * (10 ** (l-1)))
        l = l-1
    return ans


while True:
    print('\n')
    num = input('Enter any base 10 Integer: ')
    try:
        num = int(num)
        break
    except:
        print('Invalid Input')
        continue

while True:
    print('\n')
    base = input('Enter any Base from 2 to 10: ')
    try:
        base = int(base)
        if base > 1 and base <= 10:
            break
        else:
            print('Invalid Input')
            continue
    except:
        print('Invalid Input')
        continue

value = dectoanyb(num,base)
print('\n')
print(num,'in base',base,'is:',value)
print('\n')
