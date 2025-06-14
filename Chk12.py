def chk12(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b']
    for i in num:
        if i in guide:
            continue
        else:
            return 'Invalid number'
    return 'Valid'
