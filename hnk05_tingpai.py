from hnk05_hupai_abstest import HupaiCheck
from global_data import *


class TingpaiCheck:

    def __init__(self):
        self.tehai13 = [] # 注意这里的手牌变量是13张！表示的是用户的没有摸牌的手牌！
        self.machi = 0

    def machi_question(self, tehai13):
        return_ans = []
        for key in numtopai.keys():
            tehai14 = tehai13 + [key]
            tehai14.sort()
            tehai = HupaiCheck()
            tehai.numtehai = tehai14
            ans = tehai.hupai_dealall(tehai14)
            if ans != []:
                print(ans, numtopai[key],tehai14)
                return_ans += [key]
        return return_ans


if __name__ == '__main__':
    s = TingpaiCheck()
    ans = s.machi_question([1,1,1,2,3,4,5,5,6,7,8,9,9])
    print(ans)