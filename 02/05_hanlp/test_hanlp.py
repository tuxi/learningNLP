# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 11:57 PM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : test_hanlp.py
# @Software: PyCharm

import os

from jpype import *


# hanlp简称汉语言处理包，它是一系列模型与算法组成的NLP工具包，由大快搜索主导并完全开源，目标是普及自然语言处理在生产环境中的应用。HanLP具备功能完善、性能高效、架构清晰、语料时新、可自定义的特点。
# 注意：运行此demo时，需要修改路径：-Djava.class.path和`hanlp_source/hanlp.properties`中的root

if __name__=='__main__':

    from extra_libs.hanlp_source.tokenizer import start_jvm_for_hanlp

    start_jvm_for_hanlp()

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="Hanlp 分词"))
    HanLP = JClass('com.hankcs.hanlp.HanLP')

    # 中文分词
    print(HanLP.segment('从上地到西二旗怎么走'))
    print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="标准分词"))
    StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    print(StandardTokenizer.segment('从上地到西二旗怎么走'))
    print(StandardTokenizer.segment('你好，欢迎在Python中调用HanLP的API'))
    print("-" * 70)

    # NLP分词NLPTokenizer会执行全部命名实体识别和词性标注
    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="NLP分词"))
    NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
    print(NLPTokenizer.segment('北京精彩旅图科技有限公司ceo张江霖正在接待中国旅游院院长戴斌，并分享自然语言处理的心得'))
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="="*30, title="索引分词"))
    IndexTokenizer = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
    termList = IndexTokenizer.segment("主副食品")
    for term in termList:
        print(str(term) + " [" + str(term.offset) + ":" + str(term.offset + len(term.word)) + "]")
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="CRF分词"))
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="速词典分词"))
    SpeedTokenizer = JClass('com.hankcs.hanlp.tokenizer.SpeedTokenizer')
    print(NLPTokenizer.segment('江西鄱阳湖干枯，中国最大淡水湖变成大草原'))
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="自定义分词"))
    CustomDictionary = JClass('com.hankcs.hanlp.dictionary.CustomDictionary')
    text = '攻城狮逆袭单身狗，迎娶白富美，走上人生巅峰'
    print("未添加自定义词汇的结果：")
    print(HanLP.segment(text))
    CustomDictionary.add('攻城狮')
    CustomDictionary.add('单身狗')
    print("添加自定义词汇[攻城狮]和[单身狗]的结果：")
    HanLP = JClass('com.hankcs.hanlp.HanLP')
    print(HanLP.segment(text))
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="命名实体识别与词性标注"))
    NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
    print(NLPTokenizer.segment('北京精彩旅图科技有限公司ceo张江霖正在接待中国旅游院院长戴斌，并分享自然语言处理的心得'))
    print("-" * 70)

    document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
               "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
               "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
               "严格地进行水资源论证和取水许可的批准。"

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="关键词提取"))
    print(HanLP.extractKeyword(document, 8))
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="自动摘要"))
    print(HanLP.extractSummary(document, 3))
    print("-" * 70)

    print("{symbol}{title}{symbol}".format(symbol="=" * 30, title="短语提取"))
    text = r"算法工程师\n 算法（Algorithm）是一系列解决问题的清晰指令，也就是说，能够对一定规范的输入，在有限时间内获得所要求的输出。如果一个算法有缺陷，或不适合于某个问题，执行这个算法将不会解决这个问题。不同的算法可能用不同的时间、空间或效率来完成同样的任务。一个算法的优劣可以用空间复杂度与时间复杂度来衡量。算法工程师就是利用算法处理事物的人。\n \n 1职位简介\n 算法工程师是一个非常高端的职位；\n 专业要求：计算机、电子、通信、数学等相关专业；\n 学历要求：本科及其以上的学历，大多数是硕士学历及其以上；\n 语言要求：英语要求是熟练，基本上能阅读国外专业书刊；\n 必须掌握计算机相关知识，熟练使用仿真工具MATLAB等，必须会一门编程语言。\n\n2研究方向\n 视频算法工程师、图像处理算法工程师、音频算法工程师 通信基带算法工程师\n \n 3目前国内外状况\n 目前国内从事算法研究的工程师不少，但是高级算法工程师却很少，是一个非常紧缺的专业工程师。算法工程师根据研究领域来分主要有音频/视频算法处理、图像技术方面的二维信息算法处理和通信物理层、雷达信号处理、生物医学信号处理等领域的一维信息算法处理。\n 在计算机音视频和图形图像技术等二维信息算法处理方面目前比较先进的视频处理算法：机器视觉成为此类算法研究的核心；另外还有2D转3D算法(2D-to-3D conversion)，去隔行算法(de-interlacing)，运动估计运动补偿算法(Motion estimation/Motion Compensation)，去噪算法(Noise Reduction)，缩放算法(scaling)，锐化处理算法(Sharpness)，超分辨率算法(Super Resolution),手势识别(gesture recognition),人脸识别(face recognition)。\n 在通信物理层等一维信息领域目前常用的算法：无线领域的RRM、RTT，传送领域的调制解调、信道均衡、信号检测、网络优化、信号分解等。\n 另外数据挖掘、互联网搜索算法也成为当今的热门方向。\n"

    print(HanLP.extractPhrase(text, 10))
    print("-" * 70)