import operator
from global_data import *


# 2021/08/22修改 by Muqing：
# 增加了必要的注释
# 重写了hupai32_deal，手牌按照原先的方式拆分，附录部分直接读取附录形式(因为附录的拆分方式是唯一的)
# 为了读附录，hupai32_deal增加了一个参，用来传附录部分
# hupai_dealall也加了fulu的参数，有附录的不判断七对和国士
# 相应的，qidui和gsws里面不考虑绝对值的事情了，默认传进去的手牌除了进章外都是正的

# 2021/08/04修改 by Muqing:
# 修改了荔枝的胡牌判断算法，大幅提高了运行速度


class HupaiCheck:

    #  对一副3n+2的手牌的胡牌与否、胡牌拆分形式进行判断，拥有两个输入接口：self.tehai和self.numtehai，分别表示用数字字母表示的手牌和
    # 转化成了方便处理的数字形式的手牌，33332拆解形式是递归，返回存储在了self.hupaiway中，是一个最多三层嵌套的列表。如果没胡是空列表，和了的话
    # 最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成33332中的一份、或者七对子的一对，或者国士无双的所有内容。

    # 下一个版本的改进：输入不一定要输入28个字符，即2m3m4m应该被允许输入成234m，支持东南西北白发中输入
    
    def __init__(self, *, tehai='', numtehai=None):
        self.tehai = tehai              # 手牌，用mspz表示的
        if not numtehai:
            self.numtehai = []
        else:
            self.numtehai = numtehai[:]        # 手牌，用数字列表记录的东西          

        # 胡牌拆分完毕的嵌套列表，如果没胡是空列表，和了的话最大列表的第一层列表是胡牌形式，里面的每一个列表是拆分成
        # 33332中的一份、或者七对子的一对，或者国士无双的所有内容
        # 国士是两层列表
        self.hupaiway = []  

    def hupai32_deal(self, fulu=[]):
        # hupai32_deal负责将hupai函数中处理完的结果进行查重和整理
        # fulu需要传入附录部分，默认为空，格式为[ [1,2,3], [4,5,6] ]，正负不影响函数运行
        hupaidevide_unranked = []       # 胡牌分割，没有进行排序之前的部分
        hupaidevide = [] 
        
        # 将手牌里面的负值转正，因为只有一个所以处理完就break
        for i in range(len(self.numtehai)):
        	if self.numtehai[i] < 0:
        		self.numtehai[i] = -self.numtehai[i]
        		# print(self.numtehai)
        		break

        def hupai(numtehai, sorted_):
            # hupai和hupai32_deal进行一个联动，hupai是核心递归程序，将牌拆分成33332
            if len(numtehai) == 2 and numtehai[0] == numtehai[1]:
                hupaidevide_unranked.append(sorted_ + [numtehai])
            else:
                for i in range(min(4, len(numtehai))):
                    if (numtehai[i] not in numtehai[i+1:]) and (numtehai[i] + 1 in numtehai)  and (numtehai[i] + 2 in numtehai):
                        numtehainext = numtehai + []
                        i1 = numtehainext.pop(i)
                        a = numtehainext.index(i1 + 1)
                        a1 = numtehainext.pop(a)
                        b = numtehainext.index(i1 + 2)
                        b1 = numtehainext.pop(b)
                        hupai(numtehainext, sorted_ + [[i1, a1, b1]])
                for i in range(3):
                    if i + 2 < len(numtehai) and numtehai[i] == numtehai[i + 1] and numtehai[i] == numtehai[i + 2]:
                        hupai(numtehai[:i] + numtehai[i + 3:], sorted_ + [numtehai[i:i + 3]])

        hupai(self.numtehai, [])
        
        for h in hupaidevide_unranked:  #对拆牌结果从小到大进行排序
            print('h', h)
            h.sort(key=operator.itemgetter(0), reverse=False)

        for i in hupaidevide_unranked:  # 对之前找出来的胡牌方式进行去重
            if i not in hupaidevide:
                hupaidevide.append(i)

        # 最前边加上附录部分，雀头放到最后
        def my_filter(hd):
            for i in range(len(hd)):  # hd[i]是一种[33332]的拆牌型
                for j in range(len(hd[i])):  # hd[i][j]是一个顺子/克子/对子
                	if len(hd[i][j]) == 2:
                		quetou = hd[i][j]
                		hd[i].remove(quetou)
                		hd[i].append(quetou)  # 把雀头放到最后
                		break
                hd[i] = fulu + hd[i]
            return hd
        
        return my_filter(hupaidevide)

    @staticmethod
    def tehaitonumtehai(tehai, num=14):  # 字符串表示的手牌转换成数字列表的函数
        numtehai = []
        for i in range(1, num + 1):
            numtehai.append(paitonum[tehai[:2]])
            tehai = tehai[2:]
        numtehai.sort()
        return numtehai

    def qidui(self):  # 七对判断
        ans = []
        for i in range(7):
            if self.numtehai[i * 2] != self.numtehai[i * 2 + 1] or self.numtehai[i * 2] == self.numtehai[i * 2 - 1]:
                return []
            else:
                ans.append([self.numtehai[i * 2], self.numtehai[i * 2 + 1]])
        return [ans]

    def gsws(self):  # 国士判断
        gswslist = [1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]
        gscheck = self.numtehai + []
        for i in gswslist:
            if i not in gscheck:
                return []
            else:
            	gscheck.remove(i)
        if len(gscheck)==1 and gscheck[0] in gswslist:
        	return [self.numtehai]
        return []
    
    # 综合判断是否有任何一种胡牌，同样加上了附录的接口，有附录的时候不会运行self.qidui和self.gsws
    # fulu需要传入附录部分，默认为空，格式为[ [1,2,3], [4,5,6] ]，正负不影响函数运行    
    def hupai_dealall(self, fulu = []):  
        if fulu == []:
        	self.hupaiway = self.hupai32_deal(fulu) + self.qidui() + self.gsws()
        else:
        	self.hupaiway = self.hupai32_deal(fulu)
        return self.hupaiway

    def hupaiway_usersee(self):  # 荔枝写着玩的
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
    hc.numtehai = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
    print(hc.hupai_dealall())
    # print(hc.hupai32_deal())
    # hc.hupaiway_usersee()

# 已通过的测试集：
# [31,31,31,32,-32,32,34,34,34,1,2,3,4,4], fulu=[['fulu1'],['fulu2']]
# [1, 1, 2, 2, 2, 4, 5, 5, 6, 6, 7, 9, 9, 9]
# [1,1,2,2,3,3,4,4,5,5,6,6,7,7], fulu=[['fulu1'],['fulu2']]
# [1,1,2,2,3,3,4,4,5,5,6,6,7,7]
# [1,1,2,2,3,3,4,4,5,5,6,6,7,-7]
# [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
# [1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]
# [1, 1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]
# [1, 1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40], fulu=[['fulu']]
# [1, 2, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]