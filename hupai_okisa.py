from hnk05_hupai_abstest import HupaiCheck

# 6.29 2:43:fulu还是专门写出来比较好，作为可选参数带进去

class Yi:
    # 拆完的牌型
    FM_NORMAL = 0      # 33332
    FM_77 = 1          # 7对
    FM_GUOSHI = 2      # 国士

    def __init__(self):
        pass

    # 检查是否有这种役，base表示场况，是个字典
    # @abstractmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        pass

class DaSiXi(Yi):
    name = '大四喜'
    yakuman = 2
    fan = 26
    # 下位役
    down = ['小四喜']
    fuluminus = False       # 副露是否减番

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False

class GuoShi13(Yi):
    name = '国士无双十三面'
    yakuman = 2
    fan = 26
    down = ['国士无双']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_GUOSHI:
            return False

class ChunZhengJiuLian(Yi):
    name = '纯正九莲宝灯'
    yakuman = 2
    fan = 26
    down = ['九莲宝灯']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False

class SiAnKeDanJi(Yi):
    name = '四暗刻单骑'
    yakuman = 2
    fan = 26
    down = ['四暗刻']
    fuluminus = False

class XiaoSiXi(Yi):
    name = '小四喜'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

class TianHu(Yi):
    name = '天和'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

class DiHu(Yi):
    name = '地和'

class RenHu(Yi):
    name = '人和'

class SiGangZi(Yi):
    name = '四杠子'

class SiAnKe(Yi):
    name = '四暗刻'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        symbol = 0
        for tehais in tehai[:4]:
            if (tehais[0] == tehais[1] and tehais[0] == tehais[2]) and tehais[0] > 0:
                symbol += 1
        if symbol == 4:
            return True
        else:
            return False

class QingLaoTou(Yi):
    name = '清老头'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        for tehais in tehai:
            symbol = True
            for tehai in tehais:
                if abs(tehai) not in qingyaojiu:
                    symbol = False
            if not symbol:
                return False
        return True

class DaSanYuan(Yi):
    name = '大三元'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        sanyuan = 0
        for tehais in tehai:
            if tehais in [[37, 37, 37], [-37, -37, -37], [38, 38, 38], [-38, -38, -38], [40, 40, 40], [-40, -40, -40]]:
                sanyuan += 1
        if sanyuan == 3:
            return True
        return False

class HunLaoTou(Yi):
    name = '混老头'
    yakuman = 0
    fan = 2
    down = ['混全带幺九']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        # 混老头
        if format == Yi.FM_NORMAL:
            for tehais in tehai:
                symbol = True
                for tehai in tehais:
                    if abs(tehai) not in yaojiu:
                        symbol = False
                if not symbol:
                    return False
            return True
        elif format == Yi.FM_77:
            for tehais in tehai:
                symbol = True
                for tehai in tehais:
                    if abs(tehai) not in yaojiu:
                        symbol = False
                if not symbol:
                    return False
            return True
        else:
            return False

class ChunQuanDaiYaoJiu(Yi):
    name = '纯全带幺九'
    yakuman = 0
    fan = 3
    down = ['混全带幺九']
    fuluminus = True

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        # 纯全带幺九
        if not format == Yi.FM_NORMAL:
            return False
        for tehais in tehai:
            symbol = False
            for tehai in tehais:
                if abs(tehai) in qingyaojiu:
                    symbol = True
            if not symbol:
                return False
        return True

class LiangBeiKou(Yi):
    name = '两杯口'
    yakuman = 0
    fan = 2
    down = ['一杯口', '七对子']  # 两杯口一定比七对大吗
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        # 两杯口
        if not format == Yi.FM_NORMAL:
            return False
        tehai_yibeikousymbol = set(tuple(s) for s in tehai)
        tehai_yibeikousymbol = [list(t) for t in tehai_yibeikousymbol]
        tehai_yibeikousymbol.sort()
        if tehai_yibeikousymbol != tehai and fulusymbol < 2 and len(tehai_yibeikousymbol) == 3 and fulusymbol:
            return 2
        else:
            return 0


class HupaiOkisa:
    # 胡牌大小判断
    # 一番：立直s 役牌o 番牌s 断幺o 平胡s 门清自摸o 一发s 岭上开花s 海底摸月s
    # 两番：一杯口o 两立直s 一气通贯o 小三元o 三色同顺o 三色同刻o 三暗刻o 三杠子s 混全o 七对 对对o 两杯口o
    # 三番：混一色 混老头o 纯带o
    # 五番：流局满贯s
    # 六番：清一色
    # 十三番：小四喜 天和s 地和s 人和s 四杠子s 四暗刻o 清老头o 绿一色 九莲宝灯 国士无双 大三元o
    # 二十六番：大四喜 国士无双十三面 纯正九莲宝灯 四暗刻单骑s

    def __init__(self):
        self.tehai14 = []
        self.lizhi_symbol = False
        self.haidi_symbol = False
        self.gangshanghua_symbol = False
        self.gang = []
        self.akadora = []

        self.yakuman = 0   # 几倍役满
        self.fan = 0       # 几番

    def dealall(self, tehai):
        yiman = [DaSiXi, GuoShi13, ]   # 役满
        others = [DuanYaoJiu, LiZhi, ] # 其他役

        yiman_num = 0
        fan_num = 0

        # 想法得到format和场况
        format = Yi.FM_NORMAL
        base = {
            'fulu': False,
            'all_wind': 'Dong',
            'self_wind': 'Nan',
            'zimo': False
        }

        # 检查役满
        for y in yiman:
            check = y.check(tehai, format=format, base=base)
            if check:
                yiman_num += y.yakuman
                # 移除其他役种
                for i in y.down:
                    yiman.remove(i)
        
        if yiman_num > 0:
            pass
        else:
            # 算其他番

        # 宝牌

        # 算符

        # 计算得分


    def fulusymbol(self,tehai33332):
        fulus = 0
        for tehais in tehai33332:
            for tehai in tehais:
                if tehai < 0:
                    fulus += 1
        
        '''
        if fulus < 2:
            return True
        else:
            return False
        '''
        return fulus < 2

    def tanyao(self, tehai33332):
        for tehais in tehai33332:
            for tehai in tehais:
                if abs(tehai) in yaojiu:
                    return 0
        return 1

    def tyanta(self, tehai33332):
        # 混全带幺九
        for tehais in tehai33332:
            symbol = False
            for tehai in tehais:
                if abs(tehai) in yaojiu:
                    symbol = True
            if symbol == False:
                return 0

        return 1

    def haku(self, tehai33332):
        # 三元牌：白
        for tehais in tehai33332:
            if tehais in [[37, 37, 37], [-37, -37, -37]]:
                return 1
        return 0

    def hatsu(self, tehai33332):
        # 三元牌：发
        for tehais in tehai33332:
            if tehais in [[38, 38, 38], [-38, -38, -38]]:
                return 1
        return 0

    def tyun(self, tehai33332):
        # 三元牌：中
        for tehais in tehai33332:
            if tehais in [[40, 40, 40], [-40, -40, -40]]:
                return 1
        return 0


    def xiaosanyuan33332(self,tehai33332):
        # 33332形小三元
        sanyuan = 0
        for tehais in tehai33332:
            if tehais in [[37, 37, 37], [-37, -37, -37], [38, 38, 38], [-38, -38, -38], [40, 40, 40], [-40, -40, -40]]:
                sanyuan += 2
            elif tehais in [[37, 37], [38, 38], [40, 40]]:
                sanyuan += 1
        if sanyuan == 5:
            return 2
        return 0

    def xiaosanyuan77(self,tehai77):
        # 七对小三元
        sanyuan = 0
        for tehais in tehai77:
            if tehais in [[37, 37], [38, 38], [40, 40]]:
                sanyuan += 1
        if sanyuan == 3:
            return 2
        return 0

    def duidui(self,tehai33332):
        # 对对胡
        for tehais in tehai33332[:5]:
            if tehais[0] != tehais[1] or tehais[0] != tehais[2]:
                return 0
        return 2

    def sananko(self,tehai33332):
        # 三暗刻
        symbol = 0
        for tehais in tehai33332:
            if (tehais[0] == tehais[1] and tehais[0] == tehais[2]) and tehais[0] > 0:
                symbol += 1
        if symbol == 3:
            return 2

    def suanko(self,tehai33332):
        # 四暗刻
        symbol = 0
        for tehais in tehai33332[:4]:
            if (tehais[0] == tehais[1] and tehais[0] == tehais[2]) and tehais[0] > 0:
                symbol += 1
        if symbol == 4:
            return 13

    def yibeikou(self,tehai33332, fulusymbol = True):
        # 一杯口
        tehai_yibeikousymbol = set(tuple(s) for s in tehai33332)
        tehai_yibeikousymbol = [list(t) for t in tehai_yibeikousymbol]
        tehai_yibeikousymbol.sort()
        if tehai_yibeikousymbol != tehai33332 and fulusymbol < 2 and len(tehai_yibeikousymbol) == 4 and fulusymbol:
            return 1
        else:
            return 0

    def sansetongshun(self,tehai33332, fulusymbol = True):
        # 三色同顺
        for i in range(0, 5):
            for j in range(0, len(tehai33332[i])):
                if tehai33332[i][j] < 0:
                    tehai33332[i][j] *= -1
                tehai33332[i][j] = tehai33332[i][j] % 10
        tehai_sansesymbol = set(tuple(s) for s in tehai33332)
        tehai_sansesymbol = [list(t) for t in tehai_sansesymbol]
        tehai_sansesymbol2 = tehai33332 + []
        for s in tehai_sansesymbol:
            tehai_sansesymbol2.remove(s)
        print(tehai_sansesymbol, tehai_sansesymbol2)
        if len(tehai_sansesymbol) == 3 and tehai_sansesymbol2[0][0] == tehai_sansesymbol2[0][1]-1:
            if fulusymbol:
                return 2
            else:
                return 1
        else:
            return 0

    def sansetongke(self,tehai33332, fulusymbol=True):
        # 三色同刻
        for i in range(0,5):
            for j in range(0,len(tehai33332[i])):
                if tehai33332[i][j] < 0:
                    tehai33332[i][j] *= -1
                tehai33332[i][j] = tehai33332[i][j] % 10
        tehai_sansesymbol = set(tuple(s) for s in tehai33332)
        tehai_sansesymbol = [list(t) for t in tehai_sansesymbol]
        tehai_sansesymbol2 = tehai33332 + []
        for s in tehai_sansesymbol:
            tehai_sansesymbol2.remove(s)
        print(tehai_sansesymbol,tehai_sansesymbol2)
        if len(tehai_sansesymbol) == 3 and tehai_sansesymbol2[0] == tehai_sansesymbol2[1]:
            if fulusymbol:
                return 2
            else:
                return 1
        else:
            return 0

    def zumo(self,tehai33332, fulusymbol=True):
        for tehais in tehai33332:
            for tehai in tehais:
                if tehai < 0 and fulusymbol:
                    return 0
        return 1

    def yitsu(self,tehai33332, fulusymbol=True):
        # 一气通贯
        yitsusymbol = False
        for tehais in tehai33332[:4]:
            yitsusymbol = tehai33332[:4]
            yitsusymbol.remove(tehais)
            if abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[0][1] - 1) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[1][0] - 3) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[1][1] - 4) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[2][0] - 6) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[2][1] - 7):
                yitsusymbol = True
        if yitsusymbol and fulusymbol:
            return 2
        elif yitsymbol and not fulusymbol:
            return 1
        else:
            return 0

if __name__ == '__main__':

    '''
    # 断幺九测试代码
    deal = hupai_check()
    pai = hupai_okisa()
    tanyaotry = [2, 3, 4, 3, 4, 5, 6, 7, 8, 14, 15, 16, 16, 16]
    tanyao = deal.hupai_dealall(tanyaotry)
    print('tanyao', tanyao, pai.tanyao(tanyao[0]))

    # 混全带幺九测试代码
    deal = hupai_check()
    pai = hupai_okisa()
    tyantatry = [1, 2, 3, 7, 8, 9, 17, 18, 19, 21, 22, 23, 32, 32]
    tyanta = deal.hupai_dealall(tyantatry)
    print('tyanta', tyanta, pai.tyanta(tyanta[0]))

    # 纯全带幺九测试代码
    deal = hupai_check()
    pai = hupai_okisa()
    jyuntyantry = [1, 2, 3, 7, 8, 9, 17, 18, 19, 21, 22, 23, 29, 29]
    jyuntyan = deal.hupai_dealall(jyuntyantry)
    print('jyuntyan', jyuntyan, pai.jyuntyan(jyuntyan[0]))

    # 混老头测试代码
    deal = hupai_check()
    pai = hupai_okisa()
    hunlaotoutry = [1, 1, 1, 9, 9, 9, -11, -11, -11, 19, 19, 19, 34, 34]
    hunlaotou = deal.hupai_dealall(hunlaotoutry)
    print('hunlaotou', hunlaotou, pai.hunlaotou(hunlaotou[0]))

    # 清老头测试代码
    deal = hupai_check()
    pai = hupai_okisa()
    qinglaotoutry = [1, 1, 1, 9, 9, 9, 11, 11, 11, -19, -19, -19, 21, 21]
    qinglaotou = deal.hupai_dealall(qinglaotoutry)
    print('qinglaotou', qinglaotou, pai.qinglaotou(qinglaotou[0]))

    # 三元测试代码1
    deal = hupai_check()
    pai = hupai_okisa()
    sanyuantry = [37, 37, 37, 38, 38, 38, -40, -40, -40, 1, 2, 3, 4, 4]
    sanyuan = deal.hupai_dealall(sanyuantry)
    print('haku', sanyuan, pai.haku(sanyuan[0]))
    print('hatsu', sanyuan, pai.hatsu(sanyuan[0]))
    print('tyun', sanyuan, pai.tyun(sanyuan[0]))
    print('dasanyuan', sanyuan, pai.dasanyuan(sanyuan[0]))

    # 三元测试代码2
    deal = hupai_check()
    pai = hupai_okisa()
    sanyuantry = [37, 37, 37, -38, -38, -38, 4, 4, 4, 1, 2, 3, 40, 40]
    sanyuan = deal.hupai_dealall(sanyuantry)
    print('xiaosanyuan', sanyuan, pai.xiaosanyuan33332(sanyuan[0]))
    
    # 三色同顺、三色通刻测试代码
    deal = hupai_check()
    pai = hupai_okisa()
    sansetry = [37, 38, 39, -27, -28, -29, 7, 8, 9, 1, 2, 3, 8, -8]
    sanse = deal.hupai_dealall(sansetry)
    print('sanse', sanse, pai.sansetongshun(sanse[0]))
    
    # 一杯口两杯口测试代码
    deal = hupai_check()
    pai = hupai_okisa()
    yibeitry = [37, 38, 39, 37, 38, 39, 7, 8, 9, 7, 8, 9, 1, -1]
    yibei = deal.hupai_dealall(yibeitry)
    print('yibei', yibei, pai.yibeikou(yibei[0]))
    
    '''
    # 对对胡三暗刻四暗刻测试代码
    # 一气通贯测试代码
    deal = HupaiCheck()
    pai = HupaiOkisa()
    yitsutry = [11,12,13,14,15,16,-17,-18,-19,31,31,31,34,34]
    yitsu = deal.hupai_dealall(yitsutry)
    print(yitsu)
    print('yitsu', yitsu, pai.yitsu(yitsu[0]))
