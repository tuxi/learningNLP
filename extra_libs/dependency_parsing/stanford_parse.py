# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 10:20 PM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : stanford_parse.py
# @Software: PyCharm

import os, re
from stanfordcorenlp import StanfordCoreNLP
from nltk import Tree, ProbabilisticTree
import extra_libs
stanfordcorenlp_dir = os.path.join(extra_libs.extra_libs_dir, 'stanford-corenlp-full-2018-10-05')

if os.path.exists(stanfordcorenlp_dir) == False:
    raise FileNotFoundError('{path} is not found, download link: https://pan.baidu.com/s/1ep_33yssV_6wwl3SSoXxiw'.format(path=stanfordcorenlp_dir))
# 设置jar包和模型的路径
nlp = StanfordCoreNLP(path_or_host=stanfordcorenlp_dir, port=9999, lang='zh')

import nltk
grammer = "NP: {<DT>?<JJ>*<NN>}"
# 生成规则
cp = nltk.RegexpChunkParser(grammer)
pattern=re.compile(u'[^a-zA-Z\u4E00-\u9FA5]')
pattern_del=re.compile('(\a-zA-Z0-9+)')

def __replace_c(text):
    intab = ",?!()"  # 句子中有的符号，将要替换的原文
    outtab = "，？！（）" # 替换为的符号，替换以后的词，目的是将英文的符号替换为中文的符号
    deltab = " \n<li>< li>+_-.><li \U0010fc01 _"  # 删除的符号
    trantab = text.maketrans(intab, outtab,deltab)
    return text.translate(trantab)

def parse_sentence(text):
    text = __replace_c(text)
    try:
        if len(text.strip()) > 6:
            return Tree.fromstring(nlp.parse(text.strip()))
    except:
        pass


def pos(text):
    text = __replace_c(text)
    if len(text.strip()) > 6:
        return nlp.pos_tag(text)
    else:
        return False

def denpency_parse(text):
    return nlp.dependency_parse(text)

