#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 12:51 PM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : sort_dict.py
# @Software: PyCharm

import os, shutil
from extra_libs import extra_libs_dir

if __name__=='__main__':

    dict_path = os.path.join(extra_libs_dir, 'hanlp_source/data/dictionary/custom/resume_nouns.txt')
    tmp_dict_path = dict_path + '.tmp'

    # 将内容读取到d字典中
    d = {}
    with open(dict_path, 'r', encoding='utf8') as fp:
        [d.update({line: len(line.split(" ")[0])}) for line in fp]

    # 安装词的长度排序 排序时间会比较久
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)

    # 将字典d中的内容写入到tmp文件中
    with open(tmp_dict_path, 'w', encoding='utf8') as fp:
        [fp.write(item[0]) for item in sorted_dict]

    os.remove(dict_path)
    shutil.move(tmp_dict_path, dict_path)