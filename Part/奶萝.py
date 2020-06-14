from PublicReference.base_buff import *

class 奶萝技能0(被动技能):
    名称 = '人偶操纵者'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 31
    额外智力 = 0
    站街生效 = 1
    智力 = [0, 86, 90, 94, 98, 102, 107, 112, 117, 123, 129, 135, 141, 147, 154, 161, 169, 177, 185, 193, 201, 210, 219, 229, 238, 248, 258, 269, 279, 290, 301, 313, 325, 337, 349, 362, 374, 388, 401, 415, 429, 443, 458, 472, 488, 503, 519, 534, 551, 567, 584, 601, 618, 636, 653, 672, 690, 709, 728, 747, 766] 
        
    def 智力加成(self):
        return self.智力[self.等级] + self.额外智力

    def 结算统计(self): 
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立


class 奶萝技能1(主动技能):
    名称 = '小魔女的偏爱'
    所在等级 = 20
    等级上限 = 40
    基础等级 = 10
    增幅倍率 = 0.15
    def 结算统计(self):
        return [0, 0, 0, 0, 0, 0, 0, 0]

class 奶萝技能2(主动技能):
    名称 = '禁忌诅咒'
    所在等级 = 30
    等级上限 = 40
    基础等级 = 10
    BUFF力量per = 0
    BUFF智力per = 0
    BUFF物攻per = 0
    BUFF魔攻per = 0
    BUFF独立per = 0
    BUFF力量 = 0
    BUFF智力 = 0
    BUFF物攻 = 0
    BUFF魔攻 = 0
    BUFF独立 = 0
    三攻 = [0, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86]
    力智 = [0, 131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247, 256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371, 380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478]
    def 结算统计(self):
        倍率 = self.适用数值 / 665 + 1
        temp = []
        temp.append(0) #智力
        temp.append(0) #体力
        temp.append(0) #精神
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per, 3) * 倍率)) #力量
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per, 3) * 倍率)) #智力
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per, 3) * 倍率)) #物攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per, 3) * 倍率)) #魔攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per, 3) * 倍率)) #独立
        return temp

    def BUFF面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per, 0)))
        return temp


class 奶萝技能3(主动技能):
    名称 = '死命召唤'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 24
    增幅倍率 = 0.20
    def 结算统计(self): 
        return [0, 0, 0, 0, 0, 0, 0, 0]

class 奶萝技能4(被动技能):
    名称 = '少女的爱'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    额外力智 = 0
    力智 = [0, 14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442, 464, 487, 509, 532, 554, 577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892]
    def 力智加成(self):
        return self.力智[self.等级] + self.额外力智

    def 结算统计(self): 
        return [self.力智加成(), 0, 0, self.力智加成(), self.力智加成(), 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 奶萝技能5(主动技能):
    名称 = '开幕！人偶剧场'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    一觉力智 = 0
    一觉力智per = 0
    力智 = [0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 941, 993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668]
    def 结算统计(self):
        倍率 = self.适用数值 / 750 + 1
        x = (self.力智[self.等级] + self.一觉力智) * 倍率
        return [0, 0, 0, int(x * self.一觉力智per), int(x * self.一觉力智per), 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

    def 一觉面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        return temp

class 奶萝技能6(被动技能):
    名称 = '冥月绽放'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    站街生效 = 1
    智力 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]
    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self): 
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 奶萝技能7(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    站街生效 = 1
    智力 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]
    def 智力加成(self):
        return self.智力[self.等级]
    def 结算统计(self): 
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 奶萝技能8(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1
    站街生效 = 1
    智力 = [0, 40, 43, 45, 48, 50, 53, 55, 58, 60, 63, 65]
    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self): 
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立



奶萝技能列表 = []
i = 0
while i >= 0:
    try:
        exec('奶萝技能列表.append(奶萝技能'+str(i)+'())')
        i += 1
    except:
        i = -1

奶萝技能序号 = dict()
for i in range(len(奶萝技能列表)):
    奶萝技能序号[奶萝技能列表[i].名称] = i


class 奶萝角色属性(角色属性):
    职业名称 = '奶萝'
    系数类型选择 = ['智力']
    智力 = 952
    武器选项 = ['扫把']

    防具类型 = '板甲'
    防具精通属性 = ['智力']

    def __init__(self):
        self.技能栏 = copy.deepcopy(奶萝技能列表)
        self.技能序号 = copy.deepcopy(奶萝技能序号)

    def 专属词条计算(self):
        
        self.技能栏[self.技能序号['人偶操纵者']].等级加成(self.转职被动Lv)
        self.技能栏[self.技能序号['人偶操纵者']].额外智力 += self.转职被动智力

        self.技能栏[self.技能序号['死命召唤']].增幅倍率 += self.BUFF额外增幅率

        self.技能栏[self.技能序号['禁忌诅咒']].等级加成(self.BUFFLv)
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF力量per = self.BUFF力量per
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF智力per = self.BUFF智力per
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF物攻per = self.BUFF物攻per
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF魔攻per = self.BUFF魔攻per
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF独立per = self.BUFF独立per
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF力量 = self.BUFF力量
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF智力 = self.BUFF智力
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF物攻 = self.BUFF物攻
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF魔攻 = self.BUFF魔攻
        self.技能栏[self.技能序号['禁忌诅咒']].BUFF独立 = self.BUFF独立

        self.技能栏[self.技能序号['开幕！人偶剧场']].等级加成(self.一觉Lv)
        self.技能栏[self.技能序号['开幕！人偶剧场']].一觉力智 = self.一觉力智
        self.技能栏[self.技能序号['开幕！人偶剧场']].一觉力智per = self.一觉力智per

        self.技能栏[self.技能序号['少女的爱']].等级加成(self.一觉被动Lv)
        self.技能栏[self.技能序号['少女的爱']].额外力智 = self.一觉被动力智

    def BUFF计算(self, x = 0):
        self.适用数值计算()
        总数据 = []
        for i in range(len(self.技能栏)):
            if  self.次数输入[i] == '1':
                总数据.append(self.技能栏[i].结算统计())
            else:
                self.技能栏[i].增幅倍率 = 0
                总数据.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        
        for j in range(8):
            总数据[self.技能序号['禁忌诅咒']][j] = int(总数据[self.技能序号['禁忌诅咒']][j] * (1 + self.技能栏[self.技能序号['死命召唤']].增幅倍率) * (1 + self.技能栏[self.技能序号['小魔女的偏爱']].增幅倍率))

        if x==0:
            return self.提升率计算(总数据)
    
        if x==1:
            return 总数据
    
class 奶萝(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 奶萝角色属性()
        self.角色属性A = 奶萝角色属性()
        self.角色属性B = 奶萝角色属性()