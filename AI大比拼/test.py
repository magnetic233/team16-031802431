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

def move(start, opt, ft, swa, swb):
    statu = start
    p = 0
    sym = 0
    step = 0
    for i in range(9):
        if start[i] == 0:
            sym = i
            break
    print("step = %d"%step)
    print('\n')
    for i in range(3):
            print(statu[3 * i : (1 + i) * 3])
    print('\n')
##    print(statu)
##    # 隐藏交换
##    statu = swapnum(statu, 5, 6)
##    print(statu)
    for i in range(len(opt)):
        z = 0
        step += 1
        if opt[i] == 'w':
            if int(sym / 3) == 0:
                print("Error w")
                break
            else:
                z = -3
        if opt[i] == 's':
            if int(sym / 3) == 2:
                print("Error s")
                break
            else:
                z = 3
        if opt[i] == 'a':
            if sym % 3 == 0:
                print("Error a")
                break
            else:
                z = -1
        if opt[i] == 'd':
            if sym % 3 == 2:
                print("Error d")
                break
            else:
                z = 1
        if step == ft:
            if swa != swb:
                swa -= 1
                swb -= 1
                t = statu[swa]
                statu[swa] = statu[swb]
                statu[swb] = t
                for i in range(9):
                    if start[i] == 0:
                        sym = i
                        break
        statu[sym] = statu[sym + z]
        statu[sym + z] = 0
        sym += z
        print("step = %d"%step)
        print('\n')
        for i in range(3):
            print(statu[3 * i : (1 + i) * 3])
        print('\n')
        print('\n')


            
        
    

if __name__ == '__main__':
    opt = "wdsdsaawddwasdsaawwdssdwwaassdwwdssa"
    start = [9, 5, 2, 0, 3, 4, 7, 6, 1]
    step = 20
    swa = 4
    swb = 2
    move(start, opt, step, swa, swb)
    
    
