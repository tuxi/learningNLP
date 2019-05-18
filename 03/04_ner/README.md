# Named Entity Recognition
命名实体识别（Named Entity Recognition），简称NER，是自然语言处理中的一项基础任务，应用范围非常广泛。
命名实体一般指的是文本中具有特定意义或者指代性强的实体，通常包括人名、地名、组织机构名、日期时间、专有名词等。
NER系统就是从非结构化的输入文本中抽取出上述实体，并且可以按照业务需求识别出更多类别的实体，比如产品名称、型号、价格等。因此实体这个概念可以很广，只要是业务需要的特殊文本片段都可以称为实体。

- 示例
本句子很好的验证了NER的作用：
```
恩巴将参与精彩旅图举办的"旅图园"数据拓展大赛
```
`恩巴` PER
`精彩旅图` ORG
`旅图园` OTHER

学术上NER所涉及的命名实体一般包括3大类（实体类，时间类，数字类）和7小类（人名、地名、组织机构名、时间、日期、货币、百分比）。
实际应用中，NER模型通常只要识别出人名、地名、组织机构名、日期时间即可，一些系统还会给出专有名词结果（比如缩写、会议名、产品名等）。
货币、百分比等数字类实体可通过正则搞定。另外，在一些应用场景下会给出特定领域内的实体，如书名、歌曲名、期刊名等。


# 安装 nltk

下载nltk-3.4.1包
```angular2html
wget https://codeload.github.com/nltk/nltk/tar.gz/3.4.1
tar -zcvf 3.4.1
cd nltk-3.4.1
```

进入到python虚拟环境
```angular2html
workon learningNLP
```

编译nltk
```angular2html
python setup.py build
```
安装
```angular2html
python setup.py install
```

- 问题1：安装过程中如果报错中包含`python_version < "3.4"'`python_version问题。
错误堆栈：
```angular2html
(learningNLP) swaedeMacBook-Pro:nltk-develop swae$ pip install nltk
You are using pip version 7.1.0, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
Collecting nltk
  Using cached https://files.pythonhosted.org/packages/73/56/90178929712ce427ebad179f8dc46c8deef4e89d4c853092bee1efd57d05/nltk-3.4.1.zip
    Complete output from command python setup.py egg_info:
    error in nltk setup command: 'install_requires' must be a string or list of strings containing valid project/version requirement specifiers; Expected version spec in singledispatch; python_version < "3.4" at ; python_version < "3.4"

    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/p6/t42f8nmd7332018zm9m2s3d80000gn/T/pip-build-ksx1sk4q/nltk
```

解决方法：修改`setup.py`中的install_requires代码，将删除掉`'singledispatch; python_version < "3.4"'`：
```angular2html
install_requires=[
   'six',
   # 'singledispatch; python_version < "3.4"'
],
```

- 问题2：安装完成后无法`import nltk`
解决方案：
再执行一次
```angular2html
pip install nltk
```