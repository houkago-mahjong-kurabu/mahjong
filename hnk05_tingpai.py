from hnk05_hupai import hupai_check



class tingpai_check:

    def __init__(self):
        self.tehai13 = [] # 注意这里的手牌变量是13张！表示的是用户的没有摸牌的手牌！
        self.machi = 0
        global numtopai
        numtopai = {
            1: '1m', 2: '2m', 3: '3m', 4: '4m', 5: '5m', 6: '6m', 7: '7m', 8: '8m', 9: '9m',
            11: '1s', 12: '2s', 13: '3s', 14: '4s', 15: '5s', 16: '6s', 17: '7s', 18: '8s', 19: '9s',
            21: '1p', 22: '2p', 23: '3p', 24: '4p', 25: '5p', 26: '6p', 27: '7p', 28: '8p', 29: '9p',
            31: '1z', 32: '2z', 34: '3z', 35: '4z', 37: '5z', 38: '6z', 40: '7z',
        }  # 用于将牌的输入转化成数字方便处理的字典
        global paitonum
        paitonum = {
            '1m': 1, '2m': 2, '3m': 3, '4m': 4, '5m': 5, '6m': 6, '7m': 7, '8m': 8, '9m': 9,
            '1s': 11, '2s': 12, '3s': 13, '4s': 14, '5s': 15, '6s': 16, '7s': 17, '8s': 18, '9s': 19,
            '1p': 21, '2p': 22, '3p': 23, '4p': 24, '5p': 25, '6p': 26, '7p': 27, '8p': 28, '9p': 29,
            '1z': 31, '2z': 32, '3z': 34, '4z': 35, '5z': 37, '6z': 38, '7z': 40
        }  # 用于将数字转化成牌，给用户看的字典

    def machi_question(self, tehai13):
        return_ans = []
        for key in numtopai.keys():
            tehai14 = tehai13 + [key]
            tehai14.sort()
            tehai = hupai_check()
            tehai.numtehai = tehai14
            ans = tehai.hupai_dealall(tehai14)
            if ans != []:
                print(ans, numtopai[key],tehai14)
                return_ans += [key]
        return return_ans

if __name__ == '__main__':
    s = tingpai_check()
    ans = s.machi_question([1,1,1,2,3,4,5,5,6,7,8,9,9])
    print(ans)