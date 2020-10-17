import ai
import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from compare import *
from load import *          ##载入题目
##from fake import *          ##fake(aigo函数)
import time
import operator
from functools import reduce
import hehehe
global count
count = 0


# 随机字符
##ch = random.randint(1, 35)

getlist = outlist()

##outlist return([fold,chlist,locationlist,blanked])

ch = getlist[0]
# 用枚举类表示方向
class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class NumberHuaRong(QWidget):
    """ 华容道主体 """
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.zero_row = 0
        self.zero_column = 0
        self.gltMain = QGridLayout()

        self.initUI()

    def initUI(self):      
        #设置方块间隔
        self.gltMain.setSpacing(0)
##第一个参数是指布局左侧边缘向右移动，
##第二个参数是指布局上侧边缘向下移动，
##第三个参数是指布局右侧边缘向左移动，
##第四个参数是指布局下侧边缘向上移动。
##移动的都是像素点，40是指40个像素点。
        self.gltMain.setContentsMargins (0,0,0,70)
        
        self.onInit()

        # 设置布局
        self.setLayout(self.gltMain)
        # 设置宽和高
        self.setFixedSize(680, 880)
        # 设置标题
        self.setWindowTitle('爱玩不玩')
        # 设置背景颜色
        # self.setStyleSheet("border-image:url(img/beijing.jpg")
        
##        palette = QPalette()
##        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('img/beijing.jpg')))
##        self.setPalette(palette)

        #设置窗口的图标
        self.setWindowIcon(QIcon('img/hrd.ico'))

        #控件放弃思考的定义和设置
        self.buttonstop = QPushButton(self)
        self.buttonstop.setStyleSheet("QPushButton{border-image: url(img/end.png)}"
                                  "QPushButton:hover{border-image: url(img/end1.png)}" 
                                  "QPushButton:pressed{border-image: url(img/end1.png)}")
        #设置控件放弃思考的位置和大小和点击关闭
        self.buttonstop.setGeometry(500, 800, 150, 50)
        self.buttonstop.clicked.connect(self.close)

        #控件原图的定义和设置
        self.buttonroot= QPushButton(self)
        self.buttonroot.setStyleSheet("QPushButton{border-image: url(img/yuantu.png)}"
                                  "QPushButton:hover{border-image: url(img/yuantu1.png)}" 
                                  "QPushButton:pressed{border-image: url(img/yuantu1.png)}")
        #设置控件原图的位置和大小
        self.buttonroot.setGeometry(30, 800, 150, 50)

        #控件还原的定义和设置
        self.buttonauto= QPushButton(self)
        self.buttonauto.setStyleSheet("QPushButton{border-image: url(img/huanyuan.png)}"
                                  "QPushButton:hover{border-image: url(img/huanyuan1.png)}" 
                                  "QPushButton:pressed{border-image: url(img/huanyuan1.png)}")
        #设置控件还原的位置和大小
        self.buttonauto.setGeometry(220, 800, 75, 50)

        #控件打乱的定义和设置
        self.buttonmess= QPushButton(self)
        self.buttonmess.setStyleSheet("QPushButton{border-image: url(img/daluan.png)}"
                                  "QPushButton:hover{border-image: url(img/daluan1.png)}" 
                                  "QPushButton:pressed{border-image: url(img/daluan1.png)}")
        #设置控件打乱的位置和大小
        self.buttonmess.setGeometry(360, 800, 75, 50)
        
        self.show()
        
        # 初始化布局
    def onInit(self):
        # 产生顺序数组
##      self.numbers = list(range(1, 10))
##      self.blank = random.randint(1, 9)
        self.numbers = getlist[1]
        self.blank = getlist[3]
##      print(self.blank)
##      self.numbers[self.blank-1] = 0
        
        # 测试
        #print('blank = ' + str(self.blank))
        #print('ch = ' + str(ch))

        # 将数字添加到二维数组
        for row in range(3):
            self.blocks.append([])
            for column in range(3):
                temp = self.numbers[row * 3 + column]

                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)
        
##        #  打乱数组
##        for i in range(0):
##            random_num = random.randint(0, 3)
##            self.move(Direction(random_num))
        self.updatePanel()


    # 检测按键
    def keyPressEvent(self, event):
        key = event.key()
        if(key == Qt.Key_Up or key == Qt.Key_W):
            self.move(Direction.DOWN)
        if(key == Qt.Key_Down or key == Qt.Key_S):
            self.move(Direction.UP)
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.move(Direction.RIGHT)
        if(key == Qt.Key_Right or key == Qt.Key_D):
            self.move(Direction.LEFT)
        self.updatePanel()
        if self.checkResult():
            if QMessageBox.Ok == QMessageBox.information(self, '挑战结果', '恭喜您完成挑战！'):
                print("步数：",count)

        
    # 方块移动算法
    def move(self, direction):
        global count
        if(direction == Direction.UP): # 上
            if self.zero_row != 2:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row + 1][self.zero_column]
                self.blocks[self.zero_row + 1][self.zero_column] = 0
                self.zero_row += 1
                count += 1
        if(direction == Direction.DOWN): # 下
            if self.zero_row != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row - 1][self.zero_column]
                self.blocks[self.zero_row - 1][self.zero_column] = 0
                self.zero_row -= 1
                count += 1
        if(direction == Direction.LEFT): # 左
            if self.zero_column != 2:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column + 1]
                self.blocks[self.zero_row][self.zero_column + 1] = 0
                self.zero_column += 1
                count += 1
        if(direction == Direction.RIGHT): # 右
            if self.zero_column != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column - 1]
                self.blocks[self.zero_row][self.zero_column - 1] = 0
                self.zero_column -= 1
                count += 1


    def running(self):
        st = self.blocks
        bdst=[]
        bdst=(reduce(operator.add,st))
        print("还原前状态：",bdst)
        
        k=getlist               ##outlist return([fold,chlist,locationlist,blanked])
        stepandswap= loading()  #loading 返回[output['step'],output['swap'][0],output['swap'][1],uuid]
        ##    st = [8, 1, 3, 7, 0, 6, 2, 9, 5]
        st = k[1]
        ##    ta = [1, 2, 3, 0, 5, 6, 7, 9, 8]
        ta = k[2]
        print("step:",stepandswap[0])
        print("swap1:",stepandswap[1])
        print("swap2:",stepandswap[2])
        print("uuid:",stepandswap[3])
        step = stepandswap[0]
        swa = stepandswap[1]-1 ##由于传入的swp是图片编号 为了匹配数组需要-1
        swb = stepandswap[2]-1

        print(st)
        print(ta)
        print(swa)
        print(swb)
        
        caozuolist=hehehe.stp1(st, ta, step, swa+1, swb+1)
        print("操作序列:",caozuolist)
        k=len(caozuolist)
        print(k)
        
        for i in range(0,step):
          if(caozuolist[i]=='s'):
             self.move(Direction.UP)
             print("下移")
             self.updatePanel()
          if(caozuolist[i]=='w'):
             self.move(Direction.DOWN)
             print("上移")
             self.updatePanel()
          if(caozuolist[i]=='d'):
             self.move(Direction.LEFT)
             print("右移")
             self.updatePanel()
          if(caozuolist[i]=='a'):
             self.move(Direction.RIGHT)
             print("左移")
             self.updatePanel()

             
    ##此处进行交换↓
        st = self.blocks
        bdst=[]
        bdst=(reduce(operator.add,st))
        
        print("变换前状态：",bdst)
        
        print(swa)
        print(swb)
        
        betweenman = bdst[swa]
        bdst[swa] = bdst[swb]
        bdst[swb] = betweenman
        print(bdst)
        for i in range(0,3):
            for j in range(0,3):
                self.blocks[i][j]=bdst[i*3+j]                  ## 10.17 0:36  block问题 self.numbers 和blocks 不匹配 blocks为当前状态  而方块的图片取决于self number
                                                            ##应该不是numbers的问题 而是算法的隐藏交换机制 ←此段作废
        st = self.blocks
        bdst=[]
        bdst=(reduce(operator.add,st))
        print("变换后状态：",bdst)
        
    ##step交换前后↑↓

        for i in range(step,k):
          if(caozuolist[i]=='s'):
             self.move(Direction.UP)
             print("下移")
             self.updatePanel()
          if(caozuolist[i]=='w'):
             self.move(Direction.DOWN)
             print("上移")
             self.updatePanel()
          if(caozuolist[i]=='d'):
             self.move(Direction.LEFT)
             print("右移")
             self.updatePanel()
          if(caozuolist[i]=='a'):
             self.move(Direction.RIGHT)
             print("左移")
             self.updatePanel()

        st = self.blocks
        bdst=[]
        bdst=(reduce(operator.add,st))
        print("还原后状态：",bdst)

##提交文档：
        print(
            "{"
            ''' "uuid":"%s" ,'''%stepandswap[3],
          
            ''' "teamid":16 ,''',
           
            ''' "token":"d74d6a5c-409c-41d5-b066-533e48ae1425" ,''',
          
            ''' "answer":'''
                '{'
           
                ''' "operations":"%s" ,'''		%caozuolist ,
          
                ''' "swap":[%d,%d] '''	%(stepandswap[1],stepandswap[2]),
                '}'
         
            '}'
            )
        
    def daluan(self):     #  打乱数组
        st = self.blocks
        bdst=[]
        bdst=(reduce(operator.add,st))
        print("打乱前状态：",bdst)
        
        for i in range(0,30):
            random_num = random.randint(0, 3)
            if(random_num)== 0:
                self.move(Direction.UP)
                self.updatePanel()
                print("打乱")
            if(random_num)== 1:
                self.move(Direction.DOWN)
                self.updatePanel()
                print("打乱")
            if(random_num)== 2:
                self.move(Direction.LEFT)
                self.updatePanel()
                print("打乱")
            if(random_num)== 3:
                self.move(Direction.RIGHT)
                self.updatePanel()
                print("打乱")
            self.updatePanel()
            
        st = self.blocks
        bdst=[]
        bdst=(reduce(operator.add,st))
        print("打乱后当前状态：",bdst) 
            
             
    def updatePanel(self):
        for row in range(3):
            for column in range(3):
                self.gltMain.addWidget(Block(self.blocks[row][column]),row,column)

        self.setLayout(self.gltMain)

    # 检测是否完成
    def checkResult(self):
        for row in range(3):
            for column in range(3):
                if self.blocks[row][column] == row * 3 + column + 1: continue
                elif self.blocks[row][column] == 0: continue
                else: return False
        return True

class Block(QLabel):
    """ 数字方块 """

    def __init__(self, number):
        super().__init__()

        self.number = number
        # 方框大小
        self.setFixedSize(200, 200)

        # 设置字体
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)

        # 设置字体颜色
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)

        # 设置文字位置
        self.setAlignment(Qt.AlignCenter)

        # 设置背景颜色\圆角和文本内容
        self.setStyleSheet("border-image: url(ch/%d/q_%d.jpg)"%(ch, self.number))
     ##   self.setWindowOpacity(0.85)
     ##   self.setAttribute(Qt.WA_TranslucentBackground)

        
class baigei(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
       # 设置窗口的位置和大小
        self.setFixedSize(680, 680)
        # 设置窗口的标题
        self.setWindowTitle('白给华容道')
        #设置窗口的图标
        self.setWindowIcon(QIcon('img/hrd.ico'))
        #设置背景
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('img/pass.png')))
        self.setPalette(palette)

class yuantu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
       # 设置窗口的位置和大小
        self.setFixedSize(900,900)
        # 设置窗口的标题
        self.setWindowTitle('白给华容道')
        #设置窗口的图标
        self.setWindowIcon(QIcon('img/hrd.ico'))
        #设置背景
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('ch/root/%d.jpg'%ch)))
        self.setPalette(palette)
##        self.setStyleSheet("border-image: url(ch/root/%d.jpg)")
        

  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumberHuaRong()
    roottu=yuantu()
    
    ex.buttonroot.clicked.connect(roottu.show)
    ex.buttonauto.clicked.connect(ex.running)
    ex.buttonmess.clicked.connect(ex.daluan)


    count = 0
    sys.exit(app.exec_())
