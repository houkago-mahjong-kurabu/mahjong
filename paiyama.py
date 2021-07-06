from hnk05_hupai_abstest import HupaiCheck
from global_data import yaojiu, qingyaojiu, jihai, windtopai, numtopai, numtowind, windtonum
from pai import Pai
import random


class PaiYama:
    # 牌山class
    def __init__(self):
        self.yama = []  # 牌山
        self.shanpai = []  # 宝牌指示牌与里宝牌指示牌
        self.gangpai = []  # 杠的王牌
        self.dongid = 0  # 为了代码方便记录东玩家的id
        self.all_wind = 0  # 东场还是南场还是啥
        self.benchang = 0  # 几本场

    def xipai(self):
        # 完成一次牌局的关于牌山的准备工作，包括洗牌、分出宝牌和王牌。
        for i in range(0,4):
            for pais in numtopai.keys():
                self.yama.append(pais)
        random.shuffle(self.yama)
        self.gangpai = self.yama[-4:]
        self.shanpai = self.yama[-14:-4]
        self.yama = self.yama[:-14]

    def fapai(self):
        return self.yama.pop(0)

    def gang(self):
        return self.gangpai.pop(0)



if __name__ == '__main__':
    paiyama = PaiYama()
    paiyama.xipai()
    print(paiyama.yama)
    print(len(paiyama.yama))
    print(paiyama.shanpai)
    print(paiyama.gangpai)
    print('fapai:',paiyama.fapai())
    print(paiyama.yama)
    print(len(paiyama.yama))