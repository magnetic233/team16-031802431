import ai

def aigo(start, target):
    list0 = ai.bridge(start, target)
    list1 = []
    l = len(list0)
    for i in range(0, 9):
        if list0[0].digits[i] == 0:
            break
    pos = i
    column = i % 3
    row = int(i / 3)
    for i in range(1, l + 1):
        if row != 0 and list0[i - 1].digits[pos - 3] == 0:
            list1.append('w')
            row -= 1
            pos -= 3
        if row != 2 and list0[i - 1].digits[pos + 3] == 0:
            list1.append('s')
            row += 1
            pos += 3
        if column != 0 and list0[i - 1].digits[pos - 1] == 0:
            list1.append('a')
            column -= 1
            pos -= 1
        if column != 2 and list0[i - 1].digits[pos + 1] == 0:
            list1.append('d')
            column += 1
            pos += 1
    return list0, list1

def isOdd(digits):
    num = 0
    for i in range(0,9):
        if digits[i] == 0:
            continue
        for j in range(i + 1, 9):
            if digits[j] == 0:
                continue
            if digits[i] > digits[j]:
                    num += 1
    return num % 2 == 1

def swapnum(list0, a, b):
    x = 0
    y = 0
    if a != b:
        for i in range(0, 9):
            if list0[i] == a:
                x = i
            elif list0[i] == b:
                y = i
        t = list0[x]
        list0[x] = list0[y]
        list0[y] = t
    return list0

def swappos(list0, x, y):
    if x != y:
        x -= 1
        y -= 1
        t = list0[x]
        list0[x] = list0[y]
        list0[y] = t
    return list0

def find(list0, a, b):
    pa = 0
    pb = 0
    for i in range(0, 9):
        if list0[i] == a:
            pa = i
        elif list0[i] == b:
            pb = i
    return pa + 1, pb + 1

def show(digits):
    for i in range(3):
        print(digits[i * 3:(i + 1) * 3])
    print('\n')
