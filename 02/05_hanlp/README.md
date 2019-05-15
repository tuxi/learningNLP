# Hanlp 在Mac OS 的 Python 环境中安装、介绍及使用

#### Hanlp 介绍
hanlp简称汉语言处理包，它是一系列模型与算法组成的NLP工具包，由大快搜索主导并完全开源，目标是普及自然语言处理在生产环境中的应用。HanLP具备功能完善、性能高效、架构清晰、语料时新、可自定义的特点。
HanLP提供下列功能：
- 中文分词
- 词性标注
- 命名实体识别
- 关键词提取
- 自动摘要
- 短语提取
- 拼音转换
- 简繁转换
- 文本推荐
- 依存句法分析
- 文本分类
- 文本聚类
- word2vec
- 语料库工具

#### 可参考的官网链接

https://github.com/hankcs/HanLP
http://hanlp.com

#### hanlp环境安装
hanlp是java写的开源库，在python环境中调用hanlp需要java环境的支持和python调用java的工具

- 安装java
- 安装Jpype
> JPype是一个能够让 python 代码方便地调用 Java 代码的工具，从而克服了 python 在某些领域（如服务器端编程）中的不足。

```angular2html
pip install jpype1
```

- 测试环境
```angular2html
#coding=utf=8

import jpype

if __name__=='__main__':
    # 获取系统的jvm路径
    jvm_path = jpype.getDefaultJVMPath()
    # 设置jvm路径，以启动java虚拟机
    jpype.startJVM(jvm=jvm_path)
    # 执行java代码
    jpype.java.lang.System.out.println('hello world')
    # 关闭jvm虚拟机，当使用完 JVM 后，可以通过 jpype.shutdownJVM() 来关闭 JVM，该函数没有输入参数。当 python 程序退出时，JVM 会自动关闭。
    jpype.shutdownJVM()
```

打印结果：
```angular2html
hello world
JVM has been shutdown
```

至此环境配置完成

#### hanlp 安装

- [下载hanlp.jar包](https://github-production-release-asset-2e65be.s3.amazonaws.com/24976755/26040380-630e-11e9-8100-b7220f3de62a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20190515%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190515T145639Z&X-Amz-Expires=300&X-Amz-Signature=b4daf567d04b691a3d861ac1b247d4bafa5c53efe992ceba40c84b8edb40d074&X-Amz-SignedHeaders=host&actor_id=19991124&response-content-disposition=attachment%3B%20filename%3Dhanlp-1.7.3-release.zip&response-content-type=application%2Foctet-stream)
- [下载data.zip](http://file.hankcs.com/hanlp/data-for-1.7.3.zip)
下载完成后，将data.zip和hanlp-1.7.3-release.zip解压，并将解压后hanlp-1.7.3-release目录下的所有文件和的data放在同一个目录下，这里我新建一个hanlp_source的目录用于存放这些文件的
- 配置文件
hanlp的配置文件是`hanlp.properties`，配置文件的作用是告诉HanLP数据包的位置，只需修改第一行: `root=hanlp_source/`，hanlp_source必须为hanlp_source所在的路径哦。