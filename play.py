import hupai_okisa
from hnk05_hupai_abstest import HupaiCheck
from global_data import yaojiu, qingyaojiu, jihai, windtopai, numtopai, numtowind, windtonum
from pai import Pai
from player import Player
from paiyama import PaiYama
from hnk05_tingpai import TingpaiCheck
import random


def zhunbei():
    global paiyama
    paiyama = PaiYama()
    paiyama.xipai()  # 生成牌山

    global players
    players = [Player(),Player(),Player(),Player()]  # 生成四个玩家

    players[0].feng = random.randint(1,4)
    for i in range(1,4):
        players[i].feng = (players[i-1].feng + 1) % 4
        if players[i].feng == 0:
            paiyama.dongid = i
        players[i].base['all_wind'] = numtowind[paiyama.all_wind]
        players[i].base['self_wind'] = numtowind[players[i].feng]
        players[i].base['dora'] = paiyama.shanpai[0]
    # 生成四个玩家的风和base

    global whoseturn
    whoseturn = paiyama.dongid
    # 到sei了？

def fapai():
    for i in range(0,13):
        for j in range(0,4):
            players[j].tehai.append(paiyama.yama.pop(0))
    for i in range(0, 4):
        players[i].tehai.sort()
    players[paiyama.dongid].tehai.append(paiyama.yama.pop(0))
    #jd3_chupai(whoseturn)

def jd1_mopai(who):
    # 1：摸牌阶段
    players[who].tehai.append(paiyama.yama.pop(0))
    paiyama.yama.pop(0)

def jd2_zimo(who):
    # 2：自摸响应、暗杠/加杠响应、立直响应阶段之自摸
    hp = HupaiCheck()
    hp.numtehai = players[who].tehai
    if hp.hupai_dealall() != []:
        players[who].base['zimo'] = True
        print(players[who].hupaicheck(players[who].tehai,players[who].base))
    # 注意这里的hupaicheck还得再改改

def jd2_lizhi(who):
    # 2：自摸响应、暗杠/加杠响应、立直响应阶段之立直，输入该用户手牌返回可立直时的切牌
    lizhichupai = []
    for tehai in players[who].tehai:
        lizhicheck = players[who].tehai + []
        lizhicheck.remove(tehai)
        if TingpaiCheck.machi_question(lizhicheck) != []:
            lizhichupai += [tehai]
    return lizhichupai

def jd2_gang(who):
    # 2：自摸响应、暗杠/加杠响应、立直响应阶段之杠，以及随之而来的抢杠检查
    gangcheck = players[who].tehai
    for i in range(0,len(players[who].tehai)):
        gangcheck[i] = abs(gangcheck[i])
    for i in range(0,len(gangcheck)):
        if gangcheck[i] == gangcheck[i+3]:
            # ask gang or not ! ______________________________________________
            gangsymbol = input('gangma?(y/n)',gangcheck[i])
            gangpai = gangcheck[i]
            break

    # 抢杠检查
    if gangsymbol == 'y':
        for player in players:
            if player != players[who]:
                if hupai_okisa.GuoShiWuShuang.check(player.tehai+[gangpai]):
                    # ask others hu or not ! __________________________________




'''
def jd3_chupai(who):
    # 3：出牌
    pai = int(input('选择要出的牌'))
    players[who].river.append(pai)
    players[who].tehai.remove(pai)
    players[who].tehai.sort()
    '''
def jd4_otherhu(who):
    # 4：他人胡牌响应阶段
def jd5_penggang(who):
    # 5：碰杠响应阶段
def jd6_chi(who):
    # 6：吃响应阶段
def jd7_paitoriver(who):
    # 7：牌进入牌河，结束
def xingdong():
    # 考虑之后将游戏分为行动阶段：
    # 1：摸牌阶段 2：自摸响应、暗杠/加杠响应阶段 3：出牌 4：他人胡牌响应阶段 5：碰杠响应阶段 6：吃响应阶段 7：牌进入牌河，结束


'''
zhunbei()
fapai()
for i in range(0,4):
    print(players[i].feng,players[i].tehai)
for i in range(0,50):
    jd1_mopai(0)
    jd2_zimo(0)
    print(players[0].tehai)
    jd3_chupai(0)