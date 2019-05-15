#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 9:50 AM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : jieba_demo.py
# @Software: PyCharm

import jieba

'''
jieba “结巴”中文分词:是广泛使用的中文分词工具，具有以下特点:
1)三种分词模式:精确模式，全模式和搜索引擎模式
2)词性标注和返回词语在原文的起止位置( Tokenize)
3)可加入自定义字典
4)代码对 Python 2/3 均兼容
5)支持多种语言，支持简体繁体 顷目地址:https://github.com/fxsjy/jieba
'''


if __name__=='__main__':
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))