def convert(num):
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


while True:
    print('\n')
    num = input('Enter any Base 10 Integer: ')
    try:
        num = int(num)
        break
    except:
        print('Invalid Input')
        continue

result = convert(num)
print('\n')
print(num,'in Base 12 is:',result)
print('\n')
