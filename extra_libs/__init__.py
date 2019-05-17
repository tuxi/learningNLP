#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 3:00 PM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : __init__.py
# @Software: PyCharm

import os, shutil

extra_libs_dir = os.path.dirname(os.path.abspath(__file__))

def move_resume_nouns():
    '''
    resume_nouns.txt 是为hanlp准备的自定义词典
    将extra_libs/resume_nouns.txt 移动到 extra_libs/hanlp_source/data/dictionary/custom/resume_nouns.txt
    :return:
    '''
    src_path = os.path.join(extra_libs_dir, 'resume_nouns.txt')
    dst_path = os.path.join(extra_libs_dir, 'hanlp_source/data/dictionary/custom/resume_nouns.txt')
    if os.path.exists(dst_path) == True:
        print("%s be exist" % dst_path)
        return
    if not os.path.isfile(src_path):
        print("%s not exist" % src_path)
        return
    fpath, fname = os.path.split(dst_path)
    if not os.path.exists(fpath):
        print("%s not exist" % fpath)
        # os.makedirs(fpath)
        return
    shutil.copy(src=src_path, dst=dst_path)

    # 将 resume_nouns.txt;  添加到 hanlp.properties 的 CustomDictionaryPath中
    hanlp_properties = os.path.join(extra_libs_dir, 'hanlp_source/hanlp.properties')
    hanlp_properties_tmp = os.path.join(extra_libs_dir, 'hanlp_source/hanlp.properties.tmp')

    with open(hanlp_properties, 'r', encoding='utf8') as fp, open(hanlp_properties_tmp, 'w', encoding='utf8') as tmp_fp:
        # 打开两个文件： 读取hanlp_properties文件，写入hanlp_properties_tmp中
        for line in fp:
            # 循环读取hanlp_properties中的内容，将其写入到tmp文件中，写到CustomDictionaryPath这一行时，将resume_nouns.txt;插入到这一行
            key = 'CustomDictionaryPath=data/dictionary/custom/CustomDictionary.txt;'
            if key in line and 'resume_nouns.txt' not in line:
                # 将第一次匹配到key的字符替换为'CustomDictionaryPath=data/dictionary/custom/CustomDictionary.txt;resume_nouns.txt;'
                line = line.replace(key, key+" resume_nouns.txt;", 1)
            tmp_fp.write(line)

    # 将hanlp_properties_tmp 替换为  hanlp_properties_tmp
    os.remove(hanlp_properties)
    shutil.move(hanlp_properties_tmp, hanlp_properties)

    # 移除hanlp_source/data/dictionary/custom/CustomDictionary.txt.bin 清空自定义字典缓存文件，防止添加的自定义字典无效
    customDictionaryCache = os.path.join(extra_libs_dir, 'hanlp_source/data/dictionary/custom/CustomDictionary.txt.bin')
    if os.path.exists(customDictionaryCache):
        os.remove(customDictionaryCache)


move_resume_nouns()
