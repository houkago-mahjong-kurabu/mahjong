import operator
from global_data import *


class HupaiCheck:

    #   对一副具有14张牌的手牌的胡牌与否、胡牌拆分形式进行判断，拥有两个输入接口：self.tehai和self.numtehai，分别表示用数字字母表示的手牌和
    # 转化成了方便处理的数字形式的手牌，33332拆解形式是递归，返回存储在了self.hupaiway中，是一个最多三层嵌套的列表。如果没胡是空列表，和了的话
    # 最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成33332中的一份、或者七对子的一对，或者国士无双的所有内容。

    # 下一个版本的改进：输入不一定要输入28个字符，即2m3m4m应该被允许输入成234m，支持东南西北白发中输入

    # 突然发现的问题：没做吃碰杠，计划改成负数来
    def __init__(self, *, tehai='', numtehai=None):
        self.tehai = tehai              # 手牌，用mspz表示的
        if not numtehai:
            self.nunmtehai = []
        else:
            self.numtehai = numtehai[:]        # 手牌，用数字列表记录的东西          

        # 胡牌拆分完毕的嵌套列表，如果没胡是空列表，和了的话最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成
        # 33332中的一份、或者七对子的一对，或者国士无双的所有内容
        # 国士也是三层列表，这样格式统一，能省去一些田事
        self.hupaiway = []  

    def hupai32_deal(self):
        # hupai32_deal负责将hupai函数中处理完的结果进行查重和整理
        hupaidevide_unranked = []       # 胡牌分割，没有进行排序之前的部分
        hupaidevide = [] 

        def hupai(numtehai, sorted_):
            # hupai和hupai32_deal进行一个联动，hupai是核心递归程序，将牌拆分成33332
            if len(numtehai) == 2 and abs(numtehai[0]) == abs(numtehai[1]):
                hupaidevide_unranked.append(sorted_ + [numtehai])

            else:
                for i in range(len(numtehai)):
                    if (abs(numtehai[i]) + 1 in numtehai or (-(abs(numtehai[i]) + 1) in numtehai)) and\
                            ((abs(numtehai[i]) + 2 in numtehai) or (-(abs(numtehai[i]) + 2) in numtehai)):
                        numtehainext = numtehai + []

                        i1 = numtehainext.pop(i)
                        if i1 > 0:  # 这里采用怪写法的原因是希望能够尽量把负的值匹配在一起（副露了）,最后进行可行性检查
                            if abs(numtehai[i]) + 1 in numtehainext:
                                a = numtehainext.index(abs(numtehai[i]) + 1)
                            else:
                                a = numtehainext.index(-abs(numtehai[i]) - 1)
                            a1 = numtehainext.pop(a)
                            if abs(numtehai[i]) + 2 in numtehainext:
                                b = numtehainext.index(abs(numtehai[i]) + 2)
                            else:
                                b = numtehainext.index(-abs(numtehai[i]) - 2)
                        else:
                            if -abs(numtehai[i]) - 1 in numtehainext:
                                a = numtehainext.index(-abs(numtehai[i]) - 1)
                            else:
                                a = numtehainext.index(abs(numtehai[i]) + 1)
                            a1 = numtehainext.pop(a)
                            if -abs(numtehai[i]) - 2 in numtehainext:
                                b = numtehainext.index(-abs(numtehai[i]) - 2)
                            else:
                                b = numtehainext.index(abs(numtehai[i]) + 2)
                        b1 = numtehainext.pop(b)
                        hupai(numtehainext, sorted_ + [[i1, a1, b1]])
                for i in range(0, len(numtehai)):
                    if i + 2 < len(numtehai) and abs(numtehai[i]) == abs(numtehai[i + 1]) and abs(numtehai[i]) == abs(numtehai[i + 2]):
                        hupai(numtehai[:i] + numtehai[i + 3:], sorted_ + [numtehai[i:i + 3]])

        hupai(self.numtehai, [])

        for h in hupaidevide_unranked:
            h.sort(key=operator.itemgetter(0), reverse=False)

        for i in hupaidevide_unranked:
            if i not in hupaidevide:
                hupaidevide.append(i)

        # 在迭代器中使用remove会有潜在问题，可以改成filter
        def my_filter(hd):
            for i in range(len(hd)):
                # h就是之前的i[j]
                s = 0
                for k in hd[i]:
                    if k < 0:
                        s += 1
                if s == 2:
                    return False        # 认为有任何拆解形中有两张副露是不合理的，删掉！
                if len(hd[i]) == 2:
                    hd[i], hd[-1] = hd[-1], hd[i]   # 把它和最后一个交换
            return True
        
        return list(filter(my_filter, hupaidevide))

    @staticmethod
    def tehaitonumtehai(tehai, num=14):
        numtehai = []
        for i in range(1, num + 1):
            numtehai.append(paitonum[tehai[:2]])
            tehai = tehai[2:]
        numtehai.sort()
        return numtehai

    def qidui(self):
        qiduisymbol = True
        ans = []
        for i in range(7):
            if self.numtehai[i * 2] != abs(self.numtehai[i * 2 + 1]) or abs(self.numtehai[i * 2]) == abs(self.numtehai[i * 2 - 1]):
                qiduisymbol = False
            else:
                ans.append([self.numtehai[i * 2], self.numtehai[i * 2 + 1]])
        if qiduisymbol:
            return ans
        else:
            return []

    def gsws(self):
        gswslist = [1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]
        symbol = True
        for i in gswslist:
            if i not in self.numtehai:
                symbol = False
        if symbol:
            return [self.numtehai]
        else:
            return []

    def hupai_dealall(self):
        self.hupaiway = self.hupai32_deal() + self.qidui() + self.gsws()
        return self.hupaiway

    def hupaiway_usersee(self):
        if self.hupaiway != []:
            for i in self.hupaiway:
                print('胡牌方式有：')
                for j in i:
                    for k in j:
                        print(numtopai[abs(k)], end='')
                    print(' ', end='')
                print('\n')


if __name__ == '__main__':
    pai = '1m1m1m2m3m4m5m6m7m8m9m9m9m9m'
    hc = HupaiCheck(tehai=pai, numtehai=HupaiCheck.tehaitonumtehai(pai))
    hc.numtehai = [31,31,31,32,-32,32,34,34,34,1,2,3,4,4]
    hc.hupai_dealall()
    print(hc.hupai32_deal())
    hc.hupaiway_usersee()
