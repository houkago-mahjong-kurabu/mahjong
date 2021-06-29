import operator
from global_data import *


class HupaiCheck:

    # 对一副具有14张牌的手牌的胡牌与否、胡牌拆分形式进行判断，拥有两个输入接口：self.tehai和self.numtehai，分别表示用数字字母表示的手牌和
    # 转化成了方便处理的数字形式的手牌，33332拆解形式是递归，返回存储在了self.hupaiway中，是一个最多三层嵌套的列表。如果没胡是空列表，和了的话
    # 最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成33332中的一份、或者七对子的一对，或者国士无双的所有内容。

    # 下一个版本的改进：输入不一定要输入28个字符，即2m3m4m应该被允许输入成234m，支持东南西北白发中输入

    # 突然发现的问题：没做吃碰杠，计划改成负数来
    def __init__(self, *, tehai='', numtehai=[]):
        self.tehai = tehai              # 手牌，用mspz表示的
        self.numtehai = numtehai        # 手牌，用数字列表记录的东西          

        # 胡牌拆分完毕的嵌套列表，如果没胡是空列表，和了的话最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成
        # 33332中的一份、或者七对子的一对，或者国士无双的所有内容
        # 国士也是三层列表，这样格式统一，能省去一些田事
        self.hupaiway = []  

    def hupai32_deal(self):
        hupaidevide_unranked = []       # 胡牌分割，没有进行排序之前的部分
        hupaidevide = []                # 胡牌处理过程的中间变量

        def hupai(tehai, sorted_):
            if len(tehai) == 2 and tehai[0] == tehai[1]:
                hupaidevide_unranked.append(sorted_ + [tehai])

            else:
                for i in range(0, len(tehai)):
                    if tehai[i] + 1 in tehai and tehai[i] + 2 in tehai:
                        tehainext = tehai + []

                        i1 = tehainext.pop(i)
                        a = tehainext.index(tehai[i] + 1)

                        a1 = tehainext.pop(a)
                        b = tehainext.index(tehai[i] + 2)

                        b1 = tehainext.pop(b)
                        hupai(tehainext, sorted_ + [[i1, a1, b1]])
                for i in range(0, len(tehai)):
                    if i + 2 < len(tehai) and tehai[i] == tehai[i + 1] and tehai[i] == tehai[i + 2]:
                        hupai(tehai[:i] + tehai[i + 3:], sorted_ + [tehai[i:i + 3]])

        hupai(self.tehai, [])

        for h in hupaidevide_unranked:
            h.sort(key=operator.itemgetter(0), reverse=False)

        for i in hupaidevide_unranked:
            if i not in hupaidevide:
                hupaidevide.append(i)
        for i in hupaidevide:
            for j in range(len(i)):
                if len(i[j]) == 2:
                    i.append(i[j])
                    i.remove(i[j])
        
        return hupaidevide

    @staticmethod
    def tehaitonumtehai(tehai, num=14):
        numtehai = []
        for i in range(1, num + 1):
            numtehai.append(paitonum[tehai[:2]])
            tehai = tehai[2:]
        numtehai.sort()
        return numtehai

    # 如果不是七对，返回空列表
    def qidui(self):
        #qiduisymbol = True
        ans = []
        for i in range(0, 7):
            if self.tehai[i * 2] != self.tehai[i * 2 + 1] or self.tehai[i * 2] == self.tehai[i * 2 - 1]:
                pass
                # qiduisymbol = False
            else:
                ans.append([tehai[i * 2], tehai[i * 2 + 1]])
        #if qiduisymbol:
        #    return ans
        return ans

    def gsws(self):
        gswslist = [1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]
        symbol = True
        for i in gswslist:
            if i not in self.tehai:
                symbol = False
        if symbol:
            return [self.tehai]
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
                        print(numtopai[k], end='')
                    print(' ', end='')
                print('\n')


if __name__ == '__main__':
    pai = '1m1m1m2m3m4m5m6m7m8m9m9m9m1z'
    hc = HupaiCheck(tehai=pai)
    hc.hupai_dealall()
    hc.hupaiway_usersee()
    
    # pai.numtehai = [1,1,2,2,2,3,3,3,4,4,5,5,6,6]
    #print(pai.hupai32_deal(pai.numtehai))
    #print(pai.hupai_dealall(pai.numtehai))
    #print(pai.hupaiway_usersee(pai.hupai_dealall(pai.numtehai)))
