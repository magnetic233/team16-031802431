from fake import *

def stp1(start, target, step, swa, swb):
    for i in range(0, 9):
        if target[i] == 0:
            break
    sym = i
    ans = []
    list0 = []
    list1 = []
    if step == 0 or step == 1:
        start = swappos(swa, swb)
        if isOdd(start) != isOdd(target):
            print("swap(%d, %d)"%(swb, swa))
            start = swappos(swa, swb)
        (list0, list1) = aigo(start, target)
    elif isOdd(start) == isOdd(target):
        print("初始有解")
        (list0, list1) = aigo(start, target)
        statu = list0[step - 1].digits
        statu = swappos(statu, swa, swb)
        if isOdd(statu) != isOdd(target):
            print("换完无解")
            print("swap(%d, %d)"%(swb, swa))
        else:
            print("换完有解")
            ans += list1[0:step - 1]
            (list0, list1) = aigo(start, target)       
    else:
        print("初始无解")
        if sym % 3 == 0: 
            pa = sym + 2
            pb = pa + 1
        elif sym % 3 == 1:
            pa = sym
            pb = sym + 2
        elif sym % 3 == 2:
            pb = sym
            pa = pb - 1
        # 隐藏交换（此时有解）
        statu = swapnum(start, pa, pb)
        (list0, list1) = aigo(statu, target)
        statu = list0[step - 1].digits
        ans += list1[0:step - 1]
        # 任务交换
        statu = swappos(statu, swa, swb)
        if isOdd(statu) == isOdd(target):
            print("换完有解")
            # 输出隐藏位置
            (spa, spb) = find(statu, pa, pb)
            print("swap(%d, %d)"%(spb, spa))
        else:
            print("换完无解")
            # 换回隐藏
            statu = swapnum(statu, pa, pb)
            print("swap(0, 0)")
        (list0, list1) = aigo(statu, target)
    ans += list1
    str = ''.join(ans)
    return str
# 函数stp1 返回答案

if __name__ == '__main__' :
    start = [9, 5, 2, 0, 3, 4, 7, 6, 1]
    target = [1, 2, 3, 4, 5, 6, 7, 0, 9]
    step = 20
    swa = 4
    swb = 2
    print(stp1(start, target, step, swa, swb))
    
