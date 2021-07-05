from hnk05_hupai_abstest import HupaiCheck
from global_data import yaojiu, qingyaojiu, jihai, windtopai


# 6.29 2:43:fulu还是专门写出来比较好，作为可选参数带进去

class Yi:
    # 拆完的牌型
    FM_NORMAL = 0  # 33332
    FM_77 = 1  # 7对
    FM_GUOSHI = 2  # 国士

    def __init__(self):
        pass

    # 检查是否有这种役，base表示场况，是个字典
    # @abstractmethod
    def check(tehai, *, format=FM_NORMAL, base={}):
        pass


class DaSiXi(Yi):
    name = '大四喜'
    yakuman = 2
    fan = 26
    # 下位役
    down = ['小四喜']
    fuluminus = False  # 副露是否减番

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        for tehais in tehai[:4]:
            for i in range(0, len(tehais)):
                tehais[i] = abs(tehais[i])
            if tehais not in [[31, 31, 31], [32, 32, 32], [34, 34, 34], [35, 35, 35]]:
                return False
        return True


class GuoShiWuShuangShiSanMian(Yi):
    name = '国士无双十三面'
    yakuman = 2
    fan = 26
    down = ['国士无双']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_GUOSHI:
            return False
        tenkai = []
        for tehais in tehai:
            for th in tehais:
                tenkai += [th]
        tenkai.remove(base['machi'])
        if tenkai.sort() == [1, 9, 11, 19, 21, 29, 31, 32, 34, 35, 37, 38, 40]:
            return True
        return False


class ChunZhengJiuLianBaoDeng(Yi):
    name = '纯正九莲宝灯'
    yakuman = 2
    fan = 26
    down = ['九莲宝灯']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        tenkai = []
        for tehais in tehai:
            for th in tehais:
                tenkai += [th]
        tenkai.remove(base['machi'])
        if tenkai.sort() in [[1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9],
                             [11, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19],
                             [21, 21, 21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 29]]:
            return True
        return False


class SiAnKeDanJi(Yi):
    name = '四暗刻单骑'
    yakuman = 2
    fan = 26
    down = ['四暗刻']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        for tehais in tehai[:4]:
            if tehais[0] != tehais[1]:
                return False
        if tehai[5][0] == base['machi']:
            return True
        else:
            return False


class XiaoSiXi(Yi):
    name = '小四喜'
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
            for i in range(0, len(tehais)):
                tehai[i] = abs(tehai[i])
            if tehais in [[31, 31, 31], [32, 32, 32], [34, 34, 34], [35, 35, 35]]:
                symbol += 1
        tehai[4][0], tehai[4][1] = abs(tehai[4][0]), abs(tehai[4][1])
        if symbol == 3 and tehai[4] in [[31, 31], [32, 32], [34, 34], [35, 35]]:
            return True
        return False


class TianHu(Yi):
    name = '天和'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['xunmu'] == 1 and base['zifeng'] == 'dong':
            return True


class DiHu(Yi):
    name = '地和'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['xunmu'] == 1 and base['zifeng'] != 'dong' and base['zimo'] == True:
            return True


class RenHu(Yi):
    name = '人和'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['xunmu'] == 1 and base['zifeng'] != 'dong' and base['zimo'] == False:
            return True


class SiGangZi(Yi):
    name = '四杠子'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if len(base['gang']) == 4:
            return True


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
        for tehais in tehai[:4]:
            if tehais[0] != tehais[1]:
                return False
        if tehai[5][0] == base['machi']:
            return False
        else:
            return True


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


class LvYiSe(Yi):
    name = '绿一色'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        for tehais in tehai:
            for i in tehais:
                if abs(i) not in [12, 13, 14, 16, 18, 38]:
                    return False
        return True


class JiuLianBaoDeng(Yi):
    name = '九莲宝灯'
    yakuman = 1
    fan = 13
    down = ['清一色']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        jiulian = []
        for tehais in tehai:
            for i in tehais:
                jiulian += [abs(i)]
        jiuliandic = {1: [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9],
                      11: [11, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19, 19],
                      21: [21, 21, 21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 29]}
        jiuliansymbol = jiulian[0]
        try:
            for i in jiuliandic[jiuliansymbol]:
                jiulian.remove(i)
        except Exception:
            return False
        return True


class GuoShiWuShuang(Yi):
    name = '国士无双'
    yakuman = 1
    fan = 13
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        for i in range(0,len(tehai)):
            tehai[i] = abs(tehai[i])
        try:
            for i in [1,9,11,19,21,29,31,32,34,35,37,38,40]:
                tehai.remove(i)
        except Exception:
            return False
        return True



class DaSanYuan(Yi):
    name = '大三元'
    yakuman = 1
    fan = 13
    down = ['小三元']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        sanyuan = 0
        sanyuanlist = []
        for tehais in tehai:
            for i in range(0, len(tehais)):
                sanyuanlist += abs(tehais[i])
        for i in sanyuanlist:
            if i > 36:
                sanyuan += 1
        if sanyuan == 9:
            return True
        return False


class QingYiSe(Yi):
    name = '清一色'
    yakuman = 0
    fan = 6
    down = ['混一色']
    fuluminus = True

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        yisecheck = []
        for tehais in tehai:
            for i in tehais:
                yisecheck += [abs(i)]
        color = yisecheck(0) // 10
        for i in yisecheck:
            if i // 10 != color:
                return False
        return True


class HunYiSe(Yi):
    name = '混一色'
    yakuman = 0
    fan = 3
    down = []
    fuluminus = True

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        def check(tehai, *, format=Yi.FM_NORMAL, base={}):
            yisecheck = []
            for tehais in tehai:
                for i in tehais:
                    if i < 31:
                        yisecheck += [abs(i)]
            color = yisecheck(0) // 10
            for i in yisecheck:
                if i // 10 != color:
                    return False
            return True
        return True


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
        if not format == Yi.FM_NORMAL or base['fulu']:
            return False
        tehai_yibeikousymbol = set(tuple(s) for s in tehai)
        tehai_yibeikousymbol = [list(t) for t in tehai_yibeikousymbol]
        tehai_yibeikousymbol.sort()
        if tehai_yibeikousymbol != tehai and len(tehai_yibeikousymbol) == 3:
            return True
        else:
            return False


class LiangLiZhi(Yi):
    name = '两立直'
    yakuman = 0
    fan = 2
    down = ['立直']
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        return True


class YiQiTongGuan(Yi):
    name = '一气通贯'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = True

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        # 一气通贯
        yitsusignal = False
        for tehais in tehai[:4]:
            yitsusymbol = tehai[:4]
            yitsusymbol.remove(tehais)
            if abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[0][1] - 1) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[1][0] - 3) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[1][1] - 4) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[2][0] - 6) and abs(yitsusymbol[0][0]) == \
                    abs(yitsusymbol[2][1] - 7):
                yitsusignal = True
        if yitsusignal:
            return True
        else:
            return False


class XiaoSanYuan(Yi):
    name = '小三元'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if format == Yi.FM_NORMAL:
            # 33332形小三元
            sanyuan = 0
            sanyuanlist = []
            for tehais in tehai:
                for i in range(0,len(tehais)):
                    sanyuanlist += abs(tehais[i])
            for i in sanyuanlist:
                if i > 36:
                    sanyuan +=1
            if sanyuan == 8:
                return True
            return False

class SanSeTongShun(Yi):
    name = '三色同顺'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = True

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        # 三色同顺
        for i in range(0, 5):
            for j in range(0, len(tehai[i])):
                if tehai[i][j] < 0:
                    tehai[i][j] *= -1
                tehai[i][j] = tehai[i][j] % 10
        tehai_sansesymbol = set(tuple(s) for s in tehai)
        tehai_sansesymbol = [list(t) for t in tehai_sansesymbol]
        tehai_sansesymbol2 = tehai + []
        for s in tehai_sansesymbol:
            tehai_sansesymbol2.remove(s)
        # print(tehai_sansesymbol, tehai_sansesymbol2)
        if len(tehai_sansesymbol) == 3 and tehai_sansesymbol2[0][0] == tehai_sansesymbol2[0][1] - 1:
            return True
        else:
            return False


class SanSeTongKe(Yi):
    name = '三色同刻'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        # 三色同刻
        if not format == Yi.FM_NORMAL:
            return False
        for i in range(0, 5):
            for j in range(0, len(tehai[i])):
                if tehai[i][j] < 0:
                    tehai[i][j] *= -1
                tehai[i][j] = tehai[i][j] % 10
        tehai_sansesymbol = set(tuple(s) for s in tehai)
        tehai_sansesymbol = [list(t) for t in tehai_sansesymbol]
        tehai_sansesymbol2 = tehai + []
        for s in tehai_sansesymbol:
            tehai_sansesymbol2.remove(s)
        # print(tehai_sansesymbol,tehai_sansesymbol2)
        if len(tehai_sansesymbol) == 3 and tehai_sansesymbol2[0] == tehai_sansesymbol2[1]:
            return True
        else:
            return False


class SanAnKe(Yi):
    name = '三暗刻'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        # 三暗刻
        symbol = 0
        for tehais in tehai:
            if (tehais[0] == tehais[1] and tehais[0] == tehais[2]) and tehais[0] > 0:
                symbol += 1
        if symbol >= 3:
            return True
        else:
            return False


class SanGangZi(Yi):
    name = '三杠子'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        if len(base['gang']) == 3:
            return True
        else:
            return False


class HunQuanDaiYaoJiu(Yi):
    name = '混全带幺九'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = True

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        # 混全带幺九
        if not format == Yi.FM_NORMAL:
            return False
        for tehais in tehai:
            symbol = False
            for tehai in tehais:
                if abs(tehai) in yaojiu:
                    symbol = True
            if symbol == False:
                return False
        return True


class QiDuiZi(Yi):
    name = '七对子'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_77:
            return False


class DuiDuiHu(Yi):
    name = '对对和'
    yakuman = 0
    fan = 2
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        # 对对胡
        for tehais in tehai[:5]:
            if tehais[0] != tehais[1] or tehais[0] != tehais[2]:
                return False
        return True


class YiBeiKou(Yi):
    name = '一杯口'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False

        # 一杯口
        tehai_yibeikousymbol = set(tuple(s) for s in tehai)
        tehai_yibeikousymbol = [list(t) for t in tehai_yibeikousymbol]
        tehai_yibeikousymbol.sort()
        if tehai_yibeikousymbol != tehai and len(tehai_yibeikousymbol) == 4 and not base['fulu']:
            return True
        else:
            return False


class LiZhi(Yi):
    name = '立直'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['lizhi']:
            return True


class SanYuanPaiBai(Yi):
    name = '三元牌：白'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        # 三元牌：白
        for tehais in tehai:
            if tehais in [[37, 37, 37], [-37, -37, -37],[-37, 37, 37],[37,-37,37],[37,37,-37]]:
                return True
        return False


class SanYuanPaiFa(Yi):
    name = '三元牌：发'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        # 三元牌：发
        for tehais in tehai:
            if tehais in [[38, 38, 38], [-38, -38, -38],[-38,38,38],[38,-38,38],[38,38,-38]]:
                return True
        return False


class SanYuanPaiZhong(Yi):
    name = '三元牌：中'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        # 三元牌：中
        for tehais in tehai:
            if tehais in [[40, 40, 40], [-40, -40, -40],[-40,40,40],[40,-40,40],[40,40,-40]]:
                return True
        return False


class ZiFengKe(Yi):
    name = '自风刻'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        wind = windtopai[base['self_wind']]
        for tehais in tehai:
            if tehais in [[wind ,wind ,wind],[-wind,wind,wind],[-wind,-wind,-wind],[wind,-wind,wind],[wind,wind,-wind]]:
                return True
        return False


class ChangFengKe(Yi):
    name = '场风刻'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        wind = windtopai[base['all_wind']]
        for tehais in tehai:
            if tehais in [[wind, wind, wind], [-wind, wind, wind], [-wind, -wind, -wind], [wind, -wind, wind],
                          [wind, wind, -wind]]:
                return True
        return False

class DuanYaoJiu(Yi):
    name = '断幺九'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        for tehais in tehai:
            for tehai in tehais:
                if abs(tehai) in yaojiu:
                    return False
        return True


class PingHu(Yi):
    name = '平和'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if not format == Yi.FM_NORMAL:
            return False
        if tehai[4] in [[windtopai[base['all_wind']],windtopai[base['all_wind']]],[windtopai[base['self_wind']],windtopai[base['self_wind']]],[37,37],[38,38],[40,40]]:
            return False
        machi = base['machi']
        for tehais in tehai[:4]:
            if tehais[0] == tehais[1]:
                return False
            if machi in tehais:
                pinghusymbol = tehais
                pinghusymbol.remove(machi)
                if ((pinghusymbol[0] > 1 and pinghusymbol[1] < 9) or (pinghusymbol[0] > 11 and pinghusymbol[1] < 19) or (pinghusymbol[0] > 21 and pinghusymbol[1] < 29)) and pinghusymbol[0] == pinghusymbol[1] - 1:
                    return True


class MenQianQingZiMoHu(Yi):
    name = '门前清自摸和'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        return base['zimo'] and not base['fulu']


class YiFa(Yi):
    name = '一发'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['yifa'] == True:
            return True


class LingShangKaiHua(Yi):
    name = '岭上开花'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['lingshangkaihua'] == True:
            return True


class HaiDiLaoYue(Yi):
    name = '海底捞月'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['xunmu'] == 2 and base['machi'] > 0:
            return True


class HeDiLaoYu(Yi):
    name = '河底捞鱼'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        if base['xunmu'] == 2 and base['machi'] < 0:
            return True


'''class QiangGang(Yi):
    name = '抢杠'
    yakuman = 0
    fan = 1
    down = []
    fuluminus = False

    @staticmethod
    def check(tehai, *, format=Yi.FM_NORMAL, base={}):
        return True'''


nametoclass = {
    '立直': LiZhi,
    '三元牌：白': SanYuanPaiBai,
    '三元牌：中': SanYuanPaiZhong,
    '三元牌：发': SanYuanPaiBai,
    '场风刻': ChangFengKe,
    '自风刻': ZiFengKe,
    '断幺九': DuanYaoJiu,
    '平胡': PingHu,
    '一发': YiFa,
    '岭上开花': LingShangKaiHua,
    '海底捞月': HaiDiLaoYue,
    # '抢杠': QiangGang,
    '一杯口': YiBeiKou,
    '两立直': LiangLiZhi,
    '一气通贯': YiQiTongGuan,
    '小三元': XiaoSanYuan,
    '三色同顺': SanSeTongShun,
    '三色同刻': SanSeTongKe,
    '三暗刻': SanAnKe,
    '三杠子': SanGangZi,
    '混全带幺九': HunQuanDaiYaoJiu,
    '七对子': QiDuiZi,
    '对对胡': DuiDuiHu,
    '两杯口': LiangBeiKou,
    '混一色': HunYiSe,
    '混老头': HunLaoTou,
    '纯全带幺九': ChunQuanDaiYaoJiu,
    # '流局满贯': LiuJuManGuan,
    '清一色': QingYiSe,
    '小四喜': XiaoSiXi,
    '天和': TianHu,
    '地和': DiHu,
    '人和': RenHu,
    '四杠子': SiGangZi,
    '四暗刻': SiAnKe,
    '清老头': QingLaoTou,
    '绿一色': LvYiSe,
    '九莲宝灯': JiuLianBaoDeng,
    '国士无双': GuoShiWuShuang,
    '大三元': DaSanYuan,
    '大四喜': DaSiXi,
    '国士无双十三面': GuoShiWuShuangShiSanMian,
    '纯正九莲宝灯': ChunZhengJiuLianBaoDeng,
    '四暗刻单骑': SiAnKeDanJi



}


# 胡牌大小判断
# 一番：立直s 役牌o 番牌s 断幺o 平胡s 门清自摸o 一发s 岭上开花s 海底摸月s 一杯口o
# 两番：两立直s 一气通贯o 小三元o 三色同顺o 三色同刻o 三暗刻o 三杠子s 混全o 七对 对对o 两杯口o
# 三番：混一色 混老头o 纯带o
# 五番：流局满贯s
# 六番：清一色
# 十三番：小四喜 天和s 地和s 人和s 四杠子s 四暗刻o 清老头o 绿一色 九莲宝灯 国士无双 大三元o
# 二十六番：大四喜 国士无双十三面 纯正九莲宝灯 四暗刻单骑s

class HupaiOkisa:
    # 胡牌大小判断
    # 一番：立直s 役牌o 番牌s 断幺o 平胡s 门清自摸o 一发s 岭上开花s 海底摸月s
    # 两番：一杯口o 两立直s 一气通贯o 小三元o 三色同顺o 三色同刻o 三暗刻o 三杠子s 混全o 七对 对对o 两杯口o
    # 三番：混一色 混老头o 纯带o
    # 五番：流局满贯s
    # 六番：清一色
    yiman = ['大四喜', '国士无双十三面', '纯正九莲宝灯', '四暗刻单骑',
             '小四喜', '天和', '地和', '人和', '四杠子', '四暗刻', '清老头', '绿一色', '九莲宝灯',
             '国士无双', '大三元', ]

    others = ['断幺九', '立直', ]  # 其他役

    def __init__(self):
        '''
        self.tehai14 = []
        self.lizhi_symbol = False
        self.haidi_symbol = False
        self.gangshanghua_symbol = False
        self.gang = []
        self.akadora = []

        self.yakuman = 0   # 几倍役满
        self.fan = 0       # 几番
        '''
        pass

    @staticmethod
    def dealall(tehai, base):

        yiman_num = 0
        fan_num = 0

        # 判断hentai的格式是33332还是7对还是国士
        if len(tehai) == 1:
            format = Yi.FM_GUOSHI
        else:
            a, b = len(tehai[0]), len(tehai[1])
            if a == 2 and b == 2:
                format = Yi.FM_77
            else:
                format = Yi.FM_NORMAL

        # 分析是否fulu和自摸
        fulus = 0
        for tehais in tehai:
            for hai in tehais:
                if hai < 0:
                    fulus += 1
        base['fulu'] = (fulus > 2)
        base['zimo'] = (fulus % 3 == 0)

        # 检查役满
        yimanlist = HupaiOkisa.yiman + []
        for y in HupaiOkisa.yiman:
            check = y.check(tehai, format=format, base=base)
            if check:
                yiman_num += y.yakuman
                # 移除其他役种
                for i in y.down:
                    yimanlist.remove(i)

        if yiman_num > 0:
            pass
        else:
            pass
            # 算其他番

        # 宝牌
        # 算符
        # 计算得分
        return yiman_num


if __name__ == '__main__':
    # 这个应该是上层提供
    base = {
        'all_wind': 'Dong',  # 场风是啥
        'self_wind': 'Nan',  # 自风是啥
        'dora': [],  # 宝牌指示物
        'uradora': [],  # 里宝牌指示物
        'yifa': False,  # 是否一发
        'machi': '',  # 胡的哪张牌
        'gang': [],  # 杠的是嘛？明杠用负数，暗杠用正数
        'xunmu': 0,  # 巡目，从1开始，0表示随便（主要控制开关是天和地和人和以及海底河底:xunmu=012分别表示不太重要的巡目、天地人胡巡、海底巡）
        'lingshangkaihua': False,
        'fulu': False,
        'zimo': False
    }

    # 断幺九测试代码
    tests = [
        [2, 3, 4, 3, 4, 5, 6, 7, 8, 14, 15, 16, 16, 16],  # 断幺九
        [1, 2, 3, 7, 8, 9, 17, 18, 19, 21, 22, 23, 32, 32],  # 混全
    ]

    for test in tests:
        hc = HupaiCheck(numtehai=test)
        tehai_list = hc.hupai_dealall()
        print('---------')
        for tehai in tehai_list:
            print('断幺九: %s' % DuanYaoJiu.check(tehai, base=base))
            print('混全: %s' % HunQuanDaiYaoJiu.check(tehai, base=base))

    '''


    # 纯全带幺九测试代码

    jyuntyantry = [1, 2, 3, 7, 8, 9, 17, 18, 19, 21, 22, 23, 29, 29]


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

    '''
    # 对对胡三暗刻四暗刻测试代码
    # 一气通贯测试代码

    yitsutry = [11,12,13,14,15,16,-17,-18,-19,31,31,31,34,34]
    print(DaSiXi.check(yitsutry))

    '''

    '''
    hc = HupaiCheck(numtehai=yitsutry)
    hc.hupai_dealall()
    hc.hupaiway_usersee()

    deal = HupaiCheck()
    pai = HupaiOkisa()
    yitsutry = [11,12,13,14,15,16,-17,-18,-19,31,31,31,34,34]
    yitsu = deal.hupai_dealall(yitsutry)
    print(yitsu)
    print('yitsu', yitsu, pai.yitsu(yitsu[0]))
    '''
