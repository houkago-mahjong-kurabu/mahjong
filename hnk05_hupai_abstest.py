import operator


class hupai_check:

    numtopai = {
        1: '1m', 2: '2m', 3: '3m', 4: '4m', 5: '5m', 6: '6m', 7: '7m', 8: '8m', 9: '9m',
        11: '1s', 12: '2s', 13: '3s', 14: '4s', 15: '5s', 16: '6s', 17: '7s', 18: '8s', 19: '9s',
        21: '1p', 22: '2p', 23: '3p', 24: '4p', 25: '5p', 26: '6p', 27: '7p', 28: '8p', 29: '9p',
        31: '1z', 32: '2z', 34: '3z', 35: '4z', 37: '5z', 38: '6z', 40: '7z',
    }  # 用于将牌的输入转化成数字方便处理的字典
    paitonum = {
        '1m': 1, '2m': 2, '3m': 3, '4m': 4, '5m': 5, '6m': 6, '7m': 7, '8m': 8, '9m': 9,
        '1s': 11, '2s': 12, '3s': 13, '4s': 14, '5s': 15, '6s': 16, '7s': 17, '8s': 18, '9s': 19,
        '1p': 21, '2p': 22, '3p': 23, '4p': 24, '5p': 25, '6p': 26, '7p': 27, '8p': 28, '9p': 29,
        '1z': 31, '2z': 32, '3z': 34, '4z': 35, '5z': 37, '6z': 38, '7z': 40
    }  # 用于将数字转化成牌，给用户看的字典
    #   对一副具有14张牌的手牌的胡牌与否、胡牌拆分形式进行判断，拥有两个输入接口：self.tehai和self.numtehai，分别表示用数字字母表示的手牌和
    # 转化成了方便处理的数字形式的手牌，33332拆解形式是递归，返回存储在了self.hupaiway中，是一个最多三层嵌套的列表。如果没胡是空列表，和了的话
    # 最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成33332中的一份、或者七对子的一对，或者国士无双的所有内容。

    # 下一个版本的改进：输入不一定要输入28个字符，即2m3m4m应该被允许输入成234m，支持东南西北白发中输入

    # 突然发现的问题：没做吃碰杠，计划改成负数来
    def __init__(self):
        self.tehai = ''  # 手牌，用mspz表示的
        self.numtehai = []  # 手牌，用数字列表记录的东西
        self.hupaidevide_unranked = []  # 胡牌分割，没有进行排序之前的部分
        self.hupaidevide = []  # 胡牌处理过程的中间变量
        self.hupaiway = []  # 胡牌拆分完毕的嵌套列表，如果没胡是空列表，和了的话最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成
        # 33332中的一份、或者七对子的一对，或者国士无双的所有内容

    def hupai32_deal(self, tehai):
        # hupai32_deal负责将hupai函数中处理完的结果进行查重和整理
        self.hupai(tehai, [])
        for i in range(0, len(self.hupaidevide_unranked)):
            self.hupaidevide_unranked[i].sort(key=operator.itemgetter(0), reverse=False)
        for i in self.hupaidevide_unranked:
            if i not in self.hupaidevide:
                self.hupaidevide.append(i)
        for i in self.hupaidevide:
            for j in range(0, len(i)):
                s = 0
                for k in i[j]:
                    if k <0:
                        s +=1
                if s == 2:
                    self.hupaidevide.remove(i)  # 认为有任何拆解形中有两张副露是不合理的，删掉！
                    break
                if len(i[j]) == 2:
                    i.append(i[j])
                    i.remove(i[j])
        return self.hupaidevide

    def hupai(self, tehai, sorted):
        # hupai和hupai32_deal进行一个联动，hupai是核心递归程序，将牌拆分成33332
        if len(tehai) == 2 and abs(tehai[0]) == abs(tehai[1]):
            self.hupaidevide_unranked.append(sorted + [tehai])

        else:
            for i in range(0, len(tehai)):
                if (abs(tehai[i]) + 1 in tehai or (-(abs(tehai[i]) + 1) in tehai)) and\
                        ((abs(tehai[i]) + 2 in tehai) or (-(abs(tehai[i]) + 2) in tehai)):
                    tehainext = tehai + []

                    i1 = tehainext.pop(i)
                    if i1 > 0:  # 这里采用怪写法的原因是希望能够尽量把负的值匹配在一起（副露了）,最后进行可行性检查
                        try:
                            a = tehainext.index(abs(tehai[i]) + 1)
                        except Exception:
                            a = tehainext.index(-abs(tehai[i]) - 1)
                        a1 = tehainext.pop(a)
                        try:
                            b = tehainext.index(abs(tehai[i]) + 2)
                        except Exception:
                            b = tehainext.index(-abs(tehai[i]) - 2)
                    else:
                        try:
                            a = tehainext.index(-abs(tehai[i]) - 1)
                        except Exception:
                            a = tehainext.index(abs(tehai[i]) + 1)
                        a1 = tehainext.pop(a)
                        try:
                            b = tehainext.index(-abs(tehai[i]) - 2)
                        except Exception:
                            b = tehainext.index(abs(tehai[i]) + 2)
                    b1 = tehainext.pop(b)
                    self.hupai(tehainext, sorted + [[i1, a1, b1]])
            for i in range(0, len(tehai)):
                if i + 2 < len(tehai) and abs(tehai[i]) == abs(tehai[i + 1]) and abs(tehai[i]) == abs(tehai[i + 2]):
                    self.hupai(tehai[:i] + tehai[i + 3:], sorted + [tehai[i:i + 3]])

    def tehaitonumtehai(self, tehai, num=14):
        numtehai = []
        for i in range(1, num + 1):
            numtehai.append(paitonum[tehai[:2]])
            tehai = tehai[2:]
        numtehai.sort()
        return numtehai

    def qidui(self, tehai):
        qiduisymbol = True
        ans = []
        for i in range(0, 7):
            if tehai[i * 2] != abs(tehai[i * 2 + 1]) or abs(tehai[i * 2]) == abs(tehai[i * 2 - 1]):
                qiduisymbol = False
            else:
                ans.append([tehai[i * 2], tehai[i * 2 + 1]])
        if qiduisymbol:
            return ans

    def gsws(self, tehai):
        gswslist = [1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]
        symbol = True
        for i in gswslist:
            if i not in tehai:
                symbol = False
        if symbol:
            return [tehai]

    def hupai_dealall(self, tehai):
        self.hupaiway = self.hupai32_deal(tehai) + []
        try:
            self.hupaiway.append(self.qidui(tehai))
            try:
                self.hupaiway.append(self.gsws(tehai))
            except Exception:
                pass
        except Exception:
            pass
        self.hupaiway = [i for i in self.hupaiway if i != None]
        return self.hupaiway

    def hupaiway_usersee(self, hupaiway):
        if hupaiway != []:
            for i in hupaiway:
                print('胡牌方式有：')
                for j in i:
                    for k in j:
                        print(hupai_check.numtopai[abs(k)], end='')
                    print(' ', end='')
                print('\n')


if __name__ == '__main__':
    pai = hupai_check()
    # pai.tehai = '2m2m3m3m4m4m5m5m6m6m7m7m8m8m'
    # pai.numtehai = pai.tehaitonumtehai(pai.tehai)
    pai.numtehai = [2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    print(pai.hupai_dealall(pai.numtehai))
    print(pai.hupaiway_usersee(pai.hupai_dealall(pai.numtehai)))
