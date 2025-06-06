def dectoanyb(X,B):
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


while True:
    X = input('Enter any Positive Integer: ')
    try:
        X = int(X)
        break
    except:
        print('Invalid Entry')
        continue

while True:
    B = input('Enter any Base (2 to 10): ')
    try:
        B = int(B)
        if B < 2 or B > 10:
            print('Invalid Entry')
            continue
        else:
            break
    except:
        print('Invalid Entry')
        continue

result = dectoanyb(X,B)
print(result)
