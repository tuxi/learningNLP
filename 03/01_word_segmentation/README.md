# 准确分词之加载自定义字典分词

基于jieba完成示例，可查看cut_data.py.

示例中采用的是医药相关的片段，因为医药中的词有部分是生僻词，如果不加入到词典中，很难被分词。
在实际开发中，检测有哪些词没有被分词，就把它添加到字典中(dict.txt)中即可。

- 有些词即使加入到字典中，还是无法被分出，可以采用正则表达式对其进行匹配，再放入到字典中
虽然我们自定义词典并添加在jieba和hanlp中，但是某些特殊的词可能还是无法匹配到，
比如||期、III期、20% 这类词，存在多种写法，我们不能把所有的写法都加入到字典，所以使用正则表达式将这次特殊词用特殊的字符替换掉，等用jieba切完词以后，再把这些词替换回来。

- 示例cut_data.py中使用了正则表达式提取特殊字符，再使用jiebar进行分词，然后合并分词结果和特殊字符数据。
jieba使用的自定义词典在当前目录下的dict.txt中，通过调用`jieba.load_userdict('dict.txt')`加载词典。
hanlp使用的自定义词典在hanlp_source/data/dictionary/resume_nouns.txt中，通过配置`hanlp.properties`中的CustomDictionaryPath加载词典，注意需要删除缓存文件`CustomDictionary.txt.bin`

 