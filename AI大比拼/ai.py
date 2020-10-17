global ss
ss = []
global list0
list0 = []

class State:
    # h(n) 将付出的代价
    h = lambda self: 0

    def __init__(self, digits, depth, pa):
        # 数位
        self.digits = digits
        # 父状态
        self.pa = pa
        # 深度 g(n)已付出的代价
        self.depth = depth
        # 估价函数
        self.f = self.__f()

    # 交换zero位和next位的数
    def get_digits(self, zero, next):
        digits = list(self.digits)
        digits[zero] = digits[next]
        digits[next] = 0
        return digits

    # 获取可移动的下一个digits
    def next_digits(self):
        zero = [i for i, v in enumerate(self.digits) if v == 0][0]
        if int(zero / 3) != 0:
            yield self.get_digits(zero, zero-3)
            # w
        if int(zero / 3) != 2:
            yield self.get_digits(zero, zero+3)
            # s
        if zero % 3 != 0:
            yield self.get_digits(zero, zero-1)
            # a
        if zero % 3 != 2:
            yield self.get_digits(zero, zero+1)
            # d

    # 获取下一个可转换状态（父状态不在内）
    def next_state(self):
        for d in self.next_digits():
            if not self.pa or d != self.pa.digits:
                yield State(d, self.depth + 1, self)

    # 计算估价函数f(n) = g(n) + h(n)
    def __f(self):
        return self.depth + State.h(self) * 2

    # 更换h(x)
    @staticmethod
    def change_h(h):
        State.h = h
        pass

    def __eq__(self, other):
        return self.digits == other.digits

    def __str__(self):
        res = 'depth = %d, f(x) = %d\n' % (self.depth, self.f)
        for i in range(3):
            res += str(self.digits[i*3: (i+1)*3]) + '\n'
        return res

class EightDigits:
    global ss
    def __init__(self, s ):
        # 初始状态
        self.s = State(s, 0, None)
        # 目标状态
        self.e = ss
        self.open = []
        self.close = []
        self.open.append(self.s)

    # 判断奇偶排列
    def isOdd(self, digits):
        num = 0
        for i in range(9):
            if digits[i] == 0:
                continue
            for j in range(i + 1, 9):
                if digits[j] == 0:
                    continue
                if digits[i] > digits[j]:
                    num += 1
        return num % 2 == 1

    # A*算法
    def A(self):
    	# 判断可不可解
        if self.isOdd(self.s.digits) != self.isOdd(self.e):
            return None
        num = 0
        while self.open:
            front = min(self.open, key=lambda x: x.f)
            self.open.remove(front)
            num += 1
            #print(front)
            if front.digits == self.e:
            	# 搜索次数
                #print("-" * 10 + str(num) + "-" * 10 + '\n')
                return front
            self.close.append(front)
            for next in front.next_state():
                if next in self.open:
                    for i, o in enumerate(self.open):
                        if next == o:
                            if next.f < o.f:
                                self.open[i] = next
                        break
                elif next in self.close:
                    for c in self.close:
                        if next == c:
                            if next.f < c.f:
                                self.close.remove(c)
                                self.open.append(next)
                        break
                else:
                    self.open.append(next)
        return None
    
    @staticmethod
    def show(state):
        global list0
        if state.pa:
            EightDigits.show(state.pa)
        #print(state)
        list0.append(state)
        

# h函数1 代价为所有数恢复原有状态所移动距离的代价总和
def p(s):
    e = ss
    digits = s.digits
    res = 0
    for i in range(9):
        for j, v in enumerate(digits):
            if v == e[i]:
                t = abs(i - j)
                res += int(t / 3) + t % 3
                break
    return res


# h函数2 代价为不在正确位置的数的数量
def w(s):
    e = ss
    digits = s.digits
    return len([i for i in range(9) if e[i] != digits[i]])


def bridge(start, target):
    global ss
    global list0
    list0 = []
    ss = target
    State.change_h(p) # 采用h函数1
    eight_digits = EightDigits(start)
    state = eight_digits.A()
    if not state:
        print('初始状态无法移动至目标状态')
    else:
        EightDigits.show(state)

    return list0
