#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 3:49 PM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : cut_data.py
# @Software: PyCharm

import re
import os

import jieba
from extra_libs.hanlp_standard_tokenizer import cut_hanlp

# 加载自定义的字典
jieba.load_userdict('dict.txt')


def merge_two_list(a, b):
    c = []
    len_a, len_b = len(a), len(b)
    minlen = min(len_a, len_b)
    for i in range(minlen):
        c.append(a[i])
        c.append(b[i])

    if len_a > len_b:
        for i in range(minlen, len_a):
            c.append(a[i])
    else:
        for i in range(minlen, len_b):
            c.append(b[i])
    return c


if __name__ == "__main__":

    # 读取需要分析的文本片段文件
    text_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'text.txt')
    fp = open(text_path, "r", encoding="utf8")
    # 创建一个保存分析结果的文件
    fout = open("result_cut.txt", "w", encoding="utf8")

    # 虽然我们自定义词典并添加在jieba和hanlp中，但是某些特殊的词可能还是无法匹配到，
    # 比如||期、III期、20% 这类词，存在多种写法，我们不能把所有的写法都加入到字典，所以使用正则表达式将这次特殊词用特殊的字符替换掉，等用jieba切完词以后，再把这些词替换回来。

    # 第一种特殊字符： 匹配||期这种类型的词 此正则表达式用于匹配【期】字前面非汉字及部分特殊的字符
    regex1 = u'(?:[^\u4e00-\u9fa5（）*&……%￥$，,。.@! ！]){1,5}期'
    # 第二种特殊字符 匹配%的正则表达式
    regex2 = r'(?:[0-9]{1,3}[.]?[0-9]{1,3})%'
    p1 = re.compile(regex1)
    p2 = re.compile(regex2)
    for line in fp.readlines():
        result1 = p1.findall(line)
        if result1:
            regex_re1 = result1
            # 正则表达式找到匹配的值时，将此行里面的匹配值用FLAG1替换，防止后面被jieba或hanlp误切词
            # 用FLAG1替换||期、III期等期类型的词，作为占位字符
            line = p1.sub("FLAG1", line)
        result2 = p2.findall(line)
        if result2:
            # 用FLAG2替换%类型的词，比如25%、120%，作为占位字符
            line = p2.sub("FLAG2", line)
        # 用jieba进行切词，返回的是生成器
        words = jieba.cut(line)
        # 用hanlp进行切词
        # words1 = cut_hanlp(line)
        result = " ".join(words)
        if "FLAG1" in result:
            # 根据占位字符分割字符串，生成列表
            result = result.split("FLAG1")
            # 替换回来 将占位字符的原始字符合并到分词的结果中
            result = merge_two_list(result, result1)
            result = "".join(result)
        if "FLAG2" in result:
            result = result.split("FLAG2")
            result = merge_two_list(result, result2)
            result = "".join(result)
            # print(result)
        fout.write(result)
    fout.close()


