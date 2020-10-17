from PIL import Image
from PIL import ImageChops
import glob
import os
from collections import Counter


def compare_images(path_one,path_two):
    """
    比较图片
    :param path_one: 第一张图片的路径
    :param path_two: 第二张图片的路径
    :return: 相同返回 success
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one,image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            return "success"
        else:
            return "ERROR: 匹配失败！"

    except ValueError as e:
        return "{0}\n{1}".format(e,"图片大小和box对应的宽度不一致!")

def outlist():
    flag=0
    resultlist = []
    for i in range(1,10):
            for j in range(1,36):
                
                for k in range(1,9):            ##因为
                    path1="get/q_%d.jpg"%(i)
                    path2="ch/%d/q_%d.jpg"%(j,k)
                    result=compare_images(path1,path2)
                    if result == "success":
                        flag=1
                        resultlist.append(j)
                    if flag == 1:
##                        print (path1)
##                        print (path2)
##                        print ("")
                        break
                    
                if flag == 1:
                    break                  
            flag =0
##    print(resultlist)
    maxNum_sample = Counter(resultlist).most_common(1)
##  maxNum_sample[0][0] 频率最多的数字 也就是图是第x个文件夹的
##  print(maxNum_sample[0][0])
    fold=maxNum_sample[0][0]  ## fold那个文件夹里的 也就是判断出是那个字符
    print("所在文件夹:",fold)
    
    k=0
    getlist=[]
    chlist=[]
    for i in range(1,10):
        for j in range(0,10):
                    path1="get/q_%d.jpg"%(i)
                    path2="ch/%d/q_%d.jpg"%(fold,j)
                    result=compare_images(path1,path2)
                    if result == "success":
##                        print (path1)
                        getlist.append(i)
##                        print (path2)
                        chlist.append(j)
##                        print ("")
##    print("题目序号")
##    print(getlist)
##    print("顺序图 现在的状态图")
    print("当前状态:",chlist)
##判断少了那个 把目标状态的那个位置替换为0
##    [2, 6, 8, 4, 3, 9, 1, 7, 0]
##要得到的目标状态为：
##    [1, 2, 3, 4, 0, 6, 7, 8, 9]
    endflag=0
    locationlist=[1,2,3,4,5,6,7,8,9]
    blanked=0
    for i in range(0,9):
        for j in range(0,9):
            if (locationlist[i]==chlist[j]):
                break
            if (j==8):
                locationlist[i]=0
                blanked = i+1
    print("目标状态:",locationlist)
    return([fold,chlist,locationlist,blanked])
    
if __name__ == '__main__':
    k=outlist()
    print(k)

