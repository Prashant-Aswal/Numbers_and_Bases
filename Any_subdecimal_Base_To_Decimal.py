def num_check(num,base):
    i = 0
    snum = str(num)
    for n in snum:
        if int(snum[i]) > (base - 1):
            return 'Invalid Number'
            break
        else:
            i = i + 1


def convert(num,base):
    val = []
    n = 0
    sno = str(num)
    for x in sno:
        val.append(int(sno[n]))
        n = n + 1
    ans = 0
    l = len(val)
    for y in val:
        ans = ans + (y * (base ** (l - 1)))
        l = l - 1
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

result = convert(num,base)
print('\n')
print(num,'in Base',base,'is',result,'in Decimal')
print('\n')






