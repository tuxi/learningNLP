# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 11:35 AM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : ner.py
# @Software: PyCharm

from extra_libs.grammar.rules import grammer_parse

if __name__=='__main__':
    with open('text.txt', 'r', encoding='utf8') as fp, open('out.txt', 'w', encoding='utf8') as out_fp:
        [grammer_parse(line.strip(), out_fp) for line in fp if len(line.strip())>0]