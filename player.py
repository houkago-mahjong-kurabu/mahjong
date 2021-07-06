import hnk05_hupai_abstest
import hupai_okisa
from hnk05_hupai_abstest import HupaiCheck
from global_data import yaojiu, qingyaojiu, jihai, windtopai, numtopai, numtowind, windtonum
from hupai_okisa import HupaiOkisa

class Player:

    def __init__(self):
        self.id = ''  # 日后登陆id，暂时空出
        self.passwd = ''  # 日后登陆密码
        self.name = ''  # 玩家姓名
        self.gamenum = 0  # 单局游戏中使用的id1234
        self.feng = 0  # 0是东，1是南，2是西，3是北
        self.tehai = []  # 由手牌数字代号构成的列表，可以sort但是没有拆解成33332这样的东西
        self.blacktehai = []  # 没有亮出的牌，任何时刻blacktehai=tehai-fulu,用于方便输出
        self.fulu = []  # 副露记录器（方便pygame显示），负数张子的位置不同表征从不同人处获得的牌
        self.gang = []  # 开杠计张器
        self.dianshu = 25000  # 点数
        self.lizhibang = 0  # 前面有没有放立直棒？
        self.river = []  # 记录出牌的列表，普通出牌全部用正数，如果是立直牌则用负数
        self.base = {
            'all_wind': '',  # 场风是啥
            'self_wind': 'Nan',  # 自风是啥
            'dora': '',  # 宝牌指示物
            'uradora': [],  # 里宝牌指示物
            'yifa': False,  # 是否一发
            'machi': '',  # 胡的哪张牌
            'gang': [],  # 杠的是嘛？明杠用负数，暗杠用正数
            'xunmu': 1,  # 巡目，从1开始，0表示随便（主要控制开关是天和地和人和以及海底河底:xunmu=012分别表示不太重要的巡目、天地人胡巡、海底巡）
            'lingshangkaihua': False,
            'fulu': False,
            'zimo': False
        }


    def mopai(self,pai):
        # 从牌堆顶摸一张牌
        self.tehai.append(pai)

    def chupai(self):
        # 出一张牌，
        # 为了方便测试先用输入的方式出这张牌
        pai = input('输入要出的牌')
        self.tehai.remove(pai)
        self.river.append(pai)

    def hupaicheck(self,pai,base):
        hp = hnk05_hupai_abstest.HupaiCheck()
        hp.numtehai = self.tehai.append(pai)
        hp.hupai_dealall()
        if hp.hupaiway != []:
            return HupaiOkisa.dealall(hp.hupaiway,base)
        else:
            return 0
