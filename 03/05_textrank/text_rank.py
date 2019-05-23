# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 8:54 PM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : text_rank.py.py
# @Software: PyCharm

from jieba import analyse

# 引入textRank 关键字提取接口
textrank = analyse.textrank

text =  '''
        据知情人士告诉路透社，谷歌已切断了华为的安卓许可。" \
       "也就是说，华为只能使用通过开源许可公开提供的服务。\
        谷歌发言人表示，公司是「依照法规办事」，但没有透露具体细节。" \
       "但究其原因，不外乎是特朗普政府此前出台的政策，其要求将华为列入贸易黑名单。" \
       "该政策要求，黑名单上的企业未经政府许可不能从美国公司购买技术
        '''
print("\nkeyboards by textrank:")
keywords = textrank(text, topK=30, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v', 'a'), withFlag=False)
# 输出提取出的关键词，提取weight大于0.5的词
words = [keyword for keyword, weight in keywords if weight > 0.5]
print(' '.join(words) + '\n')