def chk14(num):
    num = str(num)
    guide = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']
    for i in num:
        if i in guide:
            continue
        else:
            return False
    return True
