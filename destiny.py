#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Destiny:

    k = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸',]
    
    sixty_kanshi = [
        ['甲', '子',],
        ['乙', '丑',],
        ['丙', '寅',],
        ['乙', '卯',],
        ['戊', '辰',],
        ['己', '巳',],
        ['庚', '午',],
        ['辛', '未',],
        ['壬', '申',],
        ['癸', '酉',],
        ['甲', '戌',],
        ['乙', '亥',],
        ['丙', '子',],
        ['丁', '丑',],
        ['戊', '寅',],
        ['己', '卯',],
        ['庚', '辰',],
        ['辛', '巳',],
        ['壬', '午',],
        ['癸', '未',],
        ['甲', '申',],
        ['乙', '酉',],
        ['丙', '戌',],
        ['丁', '亥',],
        ['戊', '子',],
        ['己', '丑',],
        ['庚', '寅',],
        ['辛', '卯',],
        ['壬', '辰',],
        ['癸', '巳',],
        ['甲', '午',],
        ['乙', '未',],
        ['丙', '申',],
        ['丁', '酉',],
        ['戊', '戌',],
        ['己', '亥',],
        ['庚', '子',],
        ['辛', '丑',],
        ['壬', '寅',],
        ['癸', '卯',],
        ['甲', '辰',],
        ['乙', '巳',],
        ['丙', '午',],
        ['丁', '未',],
        ['戊', '申',],
        ['己', '酉',],
        ['庚', '戌',],
        ['辛', '亥',],
        ['壬', '子',],
        ['癸', '丑',],
        ['甲', '寅',],
        ['乙', '卯',],
        ['丙', '辰',],
        ['丁', '巳',],
        ['戊', '午',],
        ['己', '未',],
        ['庚', '申',],
        ['辛', '酉',],
        ['壬', '戌',],
        ['癸', '亥',],
    ]

    kubo = [
        ['戌', '亥',],
        ['申', '酉',],
        ['午', '未',],
        ['辰', '巳',],
        ['寅', '卯',],
        ['子', '丑',],
    ]

    month_kanshi = [
        [ ['丁', '丑',],  # 甲
          ['丙', '寅',],
          ['丁', '卯',],
          ['戊', '辰',],
          ['己', '巳',],
          ['庚', '午',],
          ['辛', '未',],
          ['壬', '申',],
          ['癸', '酉',],
          ['甲', '戌',],
          ['乙', '亥',],
          ['丙', '子',], ],
        [ ['己', '丑',],  # 乙
          ['戊', '寅',],
          ['己', '卯',],
          ['庚', '辰',],
          ['辛', '巳',],
          ['壬', '午',],
          ['癸', '未',],
          ['甲', '申',],
          ['乙', '酉',],
          ['丙', '戌',],
          ['丁', '亥',],
          ['戊', '子',], ],
        [ ['辛', '丑',],  # 丙
          ['庚', '寅',],
          ['辛', '卯',],
          ['壬', '辰',],
          ['癸', '巳',],
          ['甲', '午',],
          ['乙', '未',],
          ['丙', '申',],
          ['丁', '酉',],
          ['戊', '戌',],
          ['己', '亥',],
          ['庚', '子',], ],
        [ ['癸', '丑',],  # 丁
          ['壬', '寅',],
          ['癸', '卯',],
          ['甲', '辰',],
          ['乙', '巳',],
          ['丙', '午',],
          ['丁', '未',],
          ['戊', '申',],
          ['己', '酉',],
          ['庚', '戌',],
          ['辛', '亥',],
          ['壬', '子',], ],
        [ ['乙', '丑',],  # 戊
          ['甲', '寅',],
          ['乙', '卯',],
          ['丙', '辰',],
          ['丁', '巳',],
          ['戊', '午',],
          ['己', '未',],
          ['庚', '申',],
          ['辛', '酉',],
          ['壬', '戌',],
          ['癸', '亥',],
          ['甲', '子',], ],
        [ ['丁', '丑',],  # 己
          ['丙', '寅',],
          ['丁', '卯',],
          ['戊', '辰',],
          ['己', '巳',],
          ['庚', '午',],
          ['辛', '未',],
          ['壬', '申',],
          ['癸', '酉',],
          ['甲', '戌',],
          ['乙', '亥',],
          ['丙', '子',], ],
        [ ['己', '丑',],  # 庚
          ['戊', '寅',],
          ['己', '卯',],
          ['庚', '辰',],
          ['辛', '巳',],
          ['壬', '午',],
          ['癸', '未',],
          ['甲', '申',],
          ['乙', '酉',],
          ['丙', '戌',],
          ['丁', '亥',],
          ['戊', '子',], ],
        [ ['辛', '丑',],  # 辛
          ['庚', '寅',],
          ['辛', '卯',],
          ['壬', '辰',],
          ['癸', '巳',],
          ['甲', '午',],
          ['乙', '未',],
          ['丙', '申',],
          ['丁', '酉',],
          ['戊', '戌',],
          ['己', '亥',],
          ['庚', '子',], ],
        [ ['癸', '丑',],  # 壬
          ['壬', '寅',],
          ['癸', '卯',],
          ['甲', '辰',],
          ['乙', '巳',],
          ['丙', '午',],
          ['丁', '未',],
          ['戊', '申',],
          ['己', '酉',],
          ['庚', '戌',],
          ['辛', '亥',],
          ['壬', '子',], ],
        [ ['乙', '丑',],  # 癸
          ['甲', '寅',],
          ['乙', '卯',],
          ['丙', '辰',],
          ['丁', '巳',],
          ['戊', '午',],
          ['己', '未',],
          ['庚', '申',],
          ['辛', '酉',],
          ['壬', '戌',],
          ['癸', '亥',],
          ['甲', '子',], ],
    ]

    time_kanshi = [
        ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙',], # 甲
        ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊',], # 乙
        ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚',], # 丙
        ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬',], # 丁
        ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲',], # 戊
        ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙',], # 己
        ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊',], # 庚
        ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚',], # 辛
        ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬',], # 壬
        ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲',], # 癸
    ]

    def __init__(self):
        pass
    
    def get_year_kanshi(self, year):
        return self.sixty_kanshi[(year - 3) % 60 - 1]

    def get_k_number(self, jk):
        return self.k.index(jk)
    
    def get_month_kanshi(self, jk, month):
        k_number = self.get_k_number(jk)
        return self.month_kanshi[k_number][month - 1]

    



if __name__ == '__main__':

    year = 1978
    month = 9
    day = 26
    time1 = 13
    time2 = 51

    dest = Destiny()
    
    year_kanshi = dest.get_year_kanshi(year)
    month_kanshi = dest.get_month_kanshi(year_kanshi[0], month)
    
    print(year_kanshi)
    print(month_kanshi)
