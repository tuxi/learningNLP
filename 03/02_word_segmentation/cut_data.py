#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 5:40 PM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : cut_data.py
# @Software: PyCharm

import re

import jieba
from extra_libs.hanlp_standard_tokenizer import cut_hanlp

if __name__=='__main__':

    string = '台中雨天真的很凉'
    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="未调整字典 jieba 分词 "))
    words = jieba.cut(string)
    print(" ".join(words))
    print("-" * 70)

    with open('dict.txt', 'r', encoding='utf8') as fp:
        # [jieba.suggest_freq(line.strip(), tune=True) for line in fp]
        for line in fp:
            # strip()
            # 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
            # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
            line = line.strip()

            # 调整词典
            # 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
            # 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
            # 注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。

            jieba.suggest_freq(line, tune=True)

    # 使用jieba 分词
    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="调整字典后 jieba 分词 "))
    words = jieba.cut(string)
    print(" ".join(words))
    print("-" * 70)


    # 使用hanlp 分词
    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="使用hanlp 分词"))
    words = cut_hanlp(string)
    print(words)
    print("-" * 70)