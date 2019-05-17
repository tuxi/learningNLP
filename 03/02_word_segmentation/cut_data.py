#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 5:40 PM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : cut_data.py
# @Software: PyCharm

import jieba
from extra_libs.hanlp_standard_tokenizer import cut_hanlp

# 示例需求：对`恩巴不得不回家吃饭呢`进行分词，期待的结果：`恩巴 不得不 回家 吃饭 呢`
# 示例中`恩巴`是我的名字，想要表达的意思是：今天晚上公司没有吃的，我不得不回家吃饭，
# 通过jieba进行分词，恩和巴被拆分为两个单独的词，将`恩巴`添加到jieba的自定义字典中，依旧无法识别出`恩巴`为单独的词
# 解决方案：将`恩巴`使用其他占位符替换，待jieba完成分词后再替换回去

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

if __name__=='__main__':

    string = '恩巴不得不回家吃饭呢'
    # string = '台中雨天真的很凉'
    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="未调整字典 jieba 分词 "))
    words = jieba.cut(string)
    print(" ".join(words))
    print("-" * 70)

    # 恩 巴不得 不 回家 吃饭 呢 # 这并不是我想要的，我想要的结果是：恩巴 不得不 回家 吃饭 呢
    # 即使我将`恩巴`和`不得不`添加到词典中了，依然无法得到我想要的结果
    # 最终我将这两个使用其他占位符替换，待jieba完成分词后再替换回去

    # # 生僻词
    # rare_words = ['恩巴']
    # for word in rare_words:
    #     if word in string:
    #         string = string.replace(word, 'FLAG1')

    with open('dict.txt', 'r', encoding='utf8') as fp:
        # for line in fp:
        #     # strip()
        #     # 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        #     # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        #     line = line.strip()
        #
        #     # 调整词典
        #     # 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
        #     # 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
        #     # 注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。
        #     jieba.suggest_freq(line, tune=True)

        # 对上面for循环的缩写
        [jieba.suggest_freq(line.strip(), tune=True) for line in fp]

    # 使用jieba 分词
    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="调整字典后 jieba 分词 "))
    words = jieba.cut(string)
    result = " ".join(words)
    # if 'FLAG1' in result:
    #     # 根据占位字符分割字符串，生成列表
    #     result = result.split("FLAG1")
    #     # 替换回来 将占位字符的原始字符合并到分词的结果中
    #     result = merge_two_list(result, rare_words)
    #     result = "".join(result)
    print(result)
    print("-" * 70)


    # 使用hanlp 分词
    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="使用hanlp 分词"))
    words = cut_hanlp(string)
    print(words)
    print("-" * 70)