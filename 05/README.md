章节5： N-GRAM文本挖掘
- N-Gram是基于一个假设:第n个词出现不前n-1个词相关，而不其他 任何词丌相关。(这也是隐马尔可夫当中的假设。)整个句子出现的概 率就等于各个词出现的概率乘积。各个词的概率可以通过语料中统计计 算得到。假设句子T是有词序列w1,w2,w3...wn组成，用公式表示N- Gram语言模型如下:
 
- `P(T)=P(w1)*p(w2)*p(w3)***p(wn)=p(w1)*p(w2|w1)*p(w3|w1w2)** *p(wn|w1w2w3...)`

#####一般常用的N-Gram模型是Bi-Gram和Tri-Gram。分别用公式表示如下:
- Bi-Gram: P(T)=p(w1|begin)*p(w2|w1)*p(w3|w2)***p(wn|wn-1)
- Tri-Gram: P(T)=p(w1|begin1,begin2)*p(w2|w1,begin1)*p(w3|w2w1)***p(wn| wn-1,wn-2)
- 注意上面概率的计算方法:P(w1|begin)=以w1为开头的所有句子/句 子总数;p(w2|w1)=w1,w2同时出现的次数/w1出现的次数。以此类推。

N-Gram(有时也称为N元模型)是自然语言处理中一个非常重要的概 念，通常在NLP中，人们基于一定的语料库，可以利用N-Gram来预计 戒者评估一个句子是否合理。
N-gram对中文词性标注(part of speech, POS)、中文分词(Word Segmentation)有很好的效果。中文分词和POS是中文文本分析中非 常重要的一环，因此在此作为N-gram的应用简要介绍。此外，基于N- gram还出现了更多有价值的语言模型，如NNLM、CBOW等。