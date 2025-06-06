def num_check(num,base):
    i = 0
    snum = str(num)
    for n in snum:
        if int(snum[i]) >= base:
            return 'Invalid Number'
            break
        else:
            i = i + 1


def anybtodec(X,B):
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


while True:
    print('\n')
    base = input('Enter the Base (2 to 10) of your Number: ')
    try:
        base = int(base)
        if base < 2 or base > 10:
            print('Invalid Input')
            continue
        else:
            break
    except:
        print('Invalid Input')
        continue

while True:
    print('\n')
    num = input('Enter any Integer in your selected Base: ')
    try:
        num = int(num)
        chk = num_check(num,base)
        if chk == 'Invalid Number':
            print('Entered Integer is not from the selected Base')
            continue
        else:
            break
    except:
        print('Invalid Input')
        continue

result = anybtodec(num,base)
print('\n')
print(num,'in Base',base,'is',result,'in Decimal')
print('\n')