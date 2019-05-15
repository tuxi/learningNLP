#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 11:12 AM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : ner.py
# @Software: PyCharm

# 命名实体识别(NER)是自然语言处理(NLP)中的基本任务之一

import os

from stanfordcorenlp import StanfordCoreNLP

if __name__=='__main__':

    if os.path.exists('stanford-corenlp-full-2018-10-05') == False:
        raise FileNotFoundError('stanford-corenlp-full-2018-10-05 is not found, download link: https://pan.baidu.com/s/1ep_33yssV_6wwl3SSoXxiw')
    # 设置jar包和模型的路径
    nlp = StanfordCoreNLP(path_or_host=r'stanford-corenlp-full-2018-10-05', port=9999, lang='zh')
    fin = open('news.txt', 'r', encoding='utf8')
    fner = open('ner.txt', 'w', encoding='utf8')
    ftag = open('pos_tag.txt', 'w', encoding='utf8')
    for line in fin:
        line = line.strip()
        if len(line) < 1:
            continue

        fner.write(" ".join([each[0] + "/" + each[1] for each in nlp.ner(line) if len(each) == 2]) + "\n")
        ftag.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")
    fner.close()
    ftag.close()