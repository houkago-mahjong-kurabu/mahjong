from player import Player

class GameManager:
    def __init__(self, *, players, length, ):
        """[summary]

        Args:
            players ([type]): [description]
            a ([type]): [description]
            b ([type]): [description]
        """
        self.all_wind = 0
        self.game_number = 0      # 东（南西北）几局
        self.benchang = 0         # 几本场
        self.lizhi = 0            # 立直棒有多少钱
        self.zhuang = 0           # 现在哪个田人是庄
        self.players = []         # 玩家，每个元素是一个Player对象

        self.note = None          # 负责记录游戏进程，生成录像文件


    # 开始游戏
    def play(self):
        self.start_single()


    # 单局游戏的流程控制，返回结果：[和牌的人(可能None)，听牌的人(list)]
    def start_single(self):
        self.fapai()
        # 庄家打牌
        self.chupai(self.players[self.zhuang])

    
    def end_single(self):
        # 一局游戏结束之后
        ### 这里没写好 ###
        if hu:
            if hu == self.zhuang:
                self.benchang += 1
                # 开下一局
            else:
                # 看看结不结束
                pass
        # 流局
        else:
            # 流局满贯？
            if self.zhuang in ting:
                # 连庄
                pass


    # 发牌
    def fapai(self):
        # 这里可以调用 PaiYama.fapai，或者直接在这写
        pass


    def mopai(self, player):
        # 调用 PaiYama 中的方法，给他发张牌，叫 pai
        player.mopai(pai)

        # 胡牌
        if player.hupaicheck(pai, base):
            return self.wait_zimo(player)
        else:
            return self.wait_chupai(player)



    # 进入“等待玩家响应鸣牌”的状态
    # filter: dict, 限制谁可以进行什么操作
    # 例如 0 号打了1s，1号有2s3s，2号有1s1s，同时2号和3号都听1s，则：
    # {
    #       'chi': [1]
    #       'peng': [2]
    #       'hu': [2, 3]
    # }
    def wait_mingpai(self, pai, filter_=None):
        # 这里告诉上层图形界面该如何显示按钮
        pass

    # 进入“等待玩家打牌”的状态
    # filter: 限制哪些牌可以打（比如副露牌就不能打）
    def wait_chupai(self, player, filter_=None):
        pass

    def wait_zimo(self, player):
        pass


    ### 上层回调 ###
    # event = {
    #     'player': 0,        # 0号打的
    #     'pai': 13,          # 牌的id（这里id可能要每张编号了，编号0-135，不然要想办法判断摸切还是手切）
    # }
    def callback_chupai(self, event):
        player = self.players[event['player']]
        pai = self.players[event['pai']]
        player.chupai(pai)

        # 判断一下能否鸣牌，把这俩变量填好
        mingpai = False
        filter_ = {}
        if mingpai:
            return self.wait_mingpai(pai, filter_=filter_)
        else:
            return self.mopai(self.get_next_player(player))
    

    # 获取指定玩家的下家
    def get_next_player(self, player):
        return self.players[(player.gamenum + 1) % 4]
    