#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 1:55 PM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : extract_data.py
# @Software: PyCharm

import os
from extra_libs.hanlp_standard_tokenizer import seg_sentences

if __name__=='__main__':

    with open('text.txt', 'r', encoding='utf8') as fp, \
            open('out.txt', 'w', encoding='utf8') as out_fp:
        for line in fp:
            line = line.strip()
            if len(line) > 0:
                ret = seg_sentences(line)
                content = ' '.join(ret) + '\n'
                out_fp.write(content)
