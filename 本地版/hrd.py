import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from HRD_3X3 import *
from fake import *
class Cover(QWidget):
 
    def __init__(self):
        super().__init__()
 
        self.initUI()  # 界面绘制交给InitUi方
 
    def initUI(self):
        # 设置窗口的位置和大小
        self.setFixedSize(680, 680)
        # 设置窗口的标题
        self.setWindowTitle('白给华容道')
        #设置窗口的图标
        self.setWindowIcon(QIcon('img/hrd.ico'))
    
        # 设置背景颜色
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('img/beijing.png')))
        self.setPalette(palette)
        
        # 设置标题
        self.label = QLabel(self)
        self.label.setFixedSize(360, 120)
        self.label.move(160, 100)
        self.label.setStyleSheet("QLabel{border-image: url(img/title.png)}")


        #控件buttonstart的定义和设置
        self.buttonstart = QPushButton(self)
        self.buttonstart.setStyleSheet("QPushButton{border-image: url(img/start.png)}"
                                  "QPushButton:hover{border-image: url(img/start1.png)}" 
                                  "QPushButton:pressed{border-image: url(img/start1.png)}")
        #设置控件buttonstart的位置和大小
        self.buttonstart.setGeometry(265, 260, 150, 50)

        
 
        #控件bottonexplain的定义和设置
        self.buttonexplain = QPushButton(self)
        self.buttonexplain.setStyleSheet("QPushButton{border-image: url(img/sm.png)}"
                                  "QPushButton:hover{border-image: url(img/sm1.png)}" 
                                  "QPushButton:pressed{border-image: url(img/sm1.png)}")
        #设置控件bottonexplain的位置和大小
        self.buttonexplain.setGeometry(265, 360, 150, 50)

        #控件bottonexplain的定义和设置
        self.buttonend = QPushButton(self)
        self.buttonend.setStyleSheet("QPushButton{border-image: url(img/end.png)}"
                                  "QPushButton:hover{border-image: url(img/end1.png)}" 
                                  "QPushButton:pressed{border-image: url(img/end1.png)}")
        #设置控件bottonexplain的位置和大小
        self.buttonend.setGeometry(265, 460, 150, 50)




class shuoming(QWidget):
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

        
        self.label = QLabel(self)
        self.label.setGeometry(100,0,480, 680)
        self.label.setWordWrap(True)
        self.label.setText("""
    华容道是古老的中国民间益智游戏，以其变化多端、百玩不厌的特点与魔方、独立钻石棋一起被国外智力专家并称为“智力游戏界的三个不可思议”。通过移动各个棋子，帮助曹操从初始位置移到棋盘最下方中部，从出口逃走。不允许跨越棋子，还要设法用最少的步数把曹操移到出口。曹操逃出华容道的最大障碍是关羽，关羽立马华容道，一夫当关，万夫莫开。关羽与曹操当然是解开这一游戏的关键。四个刘备军兵是最灵活的，也最容易对付，如何发挥他们的作用也要充分考虑周全。“华容道”有一个带二十个小方格的棋盘，代表华容道。
    但是这些和我们做的没有半毛钱关系。
    原始字符图片被平均切割成九份小图，并随机抠掉一张图充当空格，此时原始状态图片的顺序被打乱并拼接回去，你需要做的事就是移动白色的图片将图片恢复到原始的状态（类似数字华容道）
""")
        self.label.setStyleSheet("QLabel{font-size:18px;font-weight:normal;font-family:Arial;}")
    
        self.biaoti= QLabel(self)
        self.biaoti.setGeometry(260,20,160,150)
        self.biaoti.setText("""爱玩不玩的游戏说明""")
        self.biaoti.setStyleSheet("QLabel{font-size:18px;font-weight:normal;font-family:Arial;}")
        
        
if __name__ == '__main__':
    # 创建应用程序和对象
    
    
    app = QApplication(sys.argv)
    a = Cover()
    a.show()
    
    youxi=NumberHuaRong()
    jieshi = shuoming()
    gg=baigei()
    roottu=yuantu()
    
##华容道界面的点击效果
    youxi.buttonstop.clicked.connect(gg.show)
    youxi.buttonroot.clicked.connect(roottu.show)
    youxi.buttonauto.clicked.connect(youxi.running)
    youxi.buttonmess.clicked.connect(youxi.daluan)
##封面的三个按钮
    a.buttonstart.clicked.connect(youxi.show)
    a.buttonexplain.clicked.connect(jieshi.show)
    a.buttonend.clicked.connect(exit)

    sys.exit(app.exec_())
