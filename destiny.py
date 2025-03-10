#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Meishiki import Meishiki
from Unsei import Unsei
from Analysis import Analysis
import sys

if __name__ == "__main__":

    # 命式を作る（日干中心）
    meishiki1 = Meishiki(sys.argv, 2, "男性")
    meishiki1.build_meishiki()
    meishiki1.append_tsuhen()
    meishiki1.append_twelve_fortune()
    meishiki1.append_additional_info()

    # 命式を整形して出力する
    meishiki1.show_basic_info()
    meishiki1.show_meishiki(2)
    meishiki1.show_additional_info(True)

    # 命式を作る（用神）
    # yojin_num = 5
    # meishiki2 = Meishiki(sys.argv, yojin_num)
    # meishiki2.build_meishiki()
    # meishiki2.append_tsuhen()
    # meishiki2.append_twelve_fortune()
    # meishiki2.append_additional_info()

    # # 命式を整形して出力する
    # meishiki2.show_meishiki(yojin_num)
    # meishiki2.show_additional_info(False)

    # 運勢（大運・年運）を作る
    unsei = Unsei(meishiki1)
    unsei.append_daiun()
    unsei.append_nenun()
    unsei.append_unsei()

    # 鑑定する
    analysis = Analysis(sys.argv)

    analysis.scoring_kan(meishiki1)
    analysis.evaluate_kan_strength(meishiki1)
    analysis.show_kan_strength(meishiki1)

    # analysis.scoring_kan(meishiki2)
    # analysis.evaluate_kan_strength(meishiki2)
    # analysis.show_kan_strength(meishiki2)

    # analysis.evaluate_kan_interval(meishiki1, meishiki2)
    # analysis.evaluate_analysis_type(meishiki1, meishiki2)

    # 運勢を整形して出力する
    unsei.show_daiun_nenun()

    analysis.show_character(meishiki1)
