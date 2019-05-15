### Stanford NLP 在Mac OS 的 Python 环境中安装、介绍及使用

##### Stanford NLP 介绍
> Stanford NLP提供了一系列自然语言分析工具。它能够给出基本的 词形，词性，不管是公司名还是人名等，格式化的日期，时间，量词， 并且能够标记句子的结构，语法形式和字词依赖，指明那些名字指向同 样的实体，指明情绪，提取发言中的开放关系等。
 Stanford CoreNLP包含了中文模型，可以直接用于处理中文， 但CoreNLP使用Java开发，python调用稍微麻烦一点。

 
- 1.一个集成的语言分析工具集; 
- 2.进行快速，可靠的任意文本分析; 
- 3.整体的高质量的文本分析; 
- 4.支持多种主流语言; - 5.多种编程语言的易用接口; - 6.方便的简单的部署web服务。

##### 可参考官网链接：

https://stanfordnlp.github.io/CoreNLP/index.html
https://nlp.stanford.edu/nlp/javadoc/javanlp/
https://github.com/stanfordnlp/CoreNLP


#####  Python 版本stanford nlp 安装
> 首先需要配置JDK，安装JDK 1.8及以上版本。

- 1.安装stanford nlp自然语言处理包: 
```
pip install stanfordcorenlp
```
- 2.[下载Stanford CoreNLP文件](https://stanfordnlp.github.io/CoreNLP/download.html)
- 3.[下载中文模型jar包](https://nlp.stanford.edu/software/stanford-chinese-corenlp-2018-02-27-models.jar)
- 4.把jar包放在解压后的Stanford CoreNLP文件夹下(注意：一定要在同一目录下，否则执行会报错)
- 5.在Python中引用模型:

```
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(path_or_host=r'stanford-corenlp-full-2018-10-05', port=9999, lang='zh')

```

注意：stanford-corenlp-full-2018-10-05为模型的目录，jar包也放在此目录中，如果官网下载慢，也可以在我的网盘中下载https://pan.baidu.com/s/1ep_33yssV_6wwl3SSoXxiw
 
##### Python 版本stanford nlp 用法展示 

```
from stanfordcorenlp import StanfordCoreNLP

if __name__=='__main__':
    # 设置jar包和模型的路径
    nlp = StanfordCoreNLP(path_or_host=r'stanford-corenlp-full-2018-10-05', port=9999, lang='zh')
    fin = open('news.txt', 'r', encoding='utf8')
    fner = open('ner.txt', 'w', encoding='utf8')
    ftag = open('pos_tag.txt', 'w', encoding='utf8')
    for line in fin:
        line = line.strip()
        if len(line) < 1:
            continue

        fner.write(" ".join([each[0] + "/" + each[1] for each in nlp.ner(line) if len(each) == 2]) + "\n")
        ftag.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")
    fner.close()
    ftag.close()
```
 
 #### 错误解决
 
###### 错误1：运行StanfordCoreNLP时，报错`psutil.AccessDenied: psutil.AccessDenied (pid=14621)`错误解决办法

- 抛出异常的堆栈：

```
 Traceback (most recent call last):
  File "/Users/xiaoyuan/.virtualenvs/learningNLP/lib/python3.6/site-packages/psutil/_psosx.py", line 339, in wrapper
    return fun(self, *args, **kwargs)
  File "/Users/xiaoyuan/.virtualenvs/learningNLP/lib/python3.6/site-packages/psutil/_psosx.py", line 528, in connections
    rawlist = cext.proc_connections(self.pid, families, types)
PermissionError: [Errno 1] Operation not permitted

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Applications/PyCharm.app/Contents/helpers/pydev/pydevd.py", line 1580, in <module>
    globals = debugger.run(setup['file'], None, None, is_module)
  File "/Applications/PyCharm.app/Contents/helpers/pydev/pydevd.py", line 964, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "/Applications/PyCharm.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "/Users/xiaoyuan/Documents/GitHub/learningNLP/02/04_stanfordnlp/ner.py", line 15, in <module>
    nlp = StanfordCoreNLP(path_or_host=r'stanford-corenlp-full-2018-10-05', lang='zh')
  File "/Users/xiaoyuan/.virtualenvs/learningNLP/lib/python3.6/site-packages/stanfordcorenlp/corenlp.py", line 79, in __init__
    if port_candidate not in [conn.laddr[1] for conn in psutil.net_connections()]:
  File "/Users/xiaoyuan/.virtualenvs/learningNLP/lib/python3.6/site-packages/psutil/__init__.py", line 2263, in net_connections
    return _psplatform.net_connections(kind)
  File "/Users/xiaoyuan/.virtualenvs/learningNLP/lib/python3.6/site-packages/psutil/_psosx.py", line 252, in net_connections
    cons = Process(pid).connections(kind)
  File "/Users/xiaoyuan/.virtualenvs/learningNLP/lib/python3.6/site-packages/psutil/_psosx.py", line 344, in wrapper
    raise AccessDenied(self.pid, self._name)
psutil.AccessDenied: psutil.AccessDenied (pid=14621)
```

- 解决方法：此方法适用于mac os平台
找到`stanfordcorenlp`这个package的`corenlp.py`（如果是通过pip安装的stanfordcorenlp，那么corenlp.py在`site-packages/stanfordcorenlp`目录下），将第84和85行代码注释或删除即可，就是下面两行
```
if self.port in [conn.laddr[1] for conn in psutil.net_connections()]:
   raise IOError('Port ' + str(self.port) + ' is already in use.')
```
并在初始化`StanfordCoreNLP`，指定port端口
最后重新执行`python ner.py`即可。