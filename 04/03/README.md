### 自定义语法与CFG

##### 什么是语法解析?
- 在自然语言学习过程中，每个人一定都学过语法，例如句子可以用主语、 谓语、宾语来表示。在自然语言的处理过程中，有许多应用场景都需要 考虑句子的语法，因此研究语法解析变得非常重要。
- 语法解析有两个主要的问题，其一是句子语法在计算机中的表达不存储 方法，以及语料数据集;其二是语法解析的算法。
- 对于第一个问题，我们可以用树状结构图来表示，如下图所示，S表示 句子;NP、VP、PP是名词、动词、介词短语(短语级别);N、V、P 分别是名词、动词、介词。

##### 上下文无关语法(Context-Free Grammer)
> 为了生成句子的语法树，我们可以定义如下的一套上下文无关语法。

- 1. N表示一组非叶子节点的标注，例如{S、NP、VP、N...}
- 2. Σ表示一组叶子结点的标注，例如{boeing、is...}
- 3. R表示一组觃则，每条觃则可以表示为
- 4. S表示语法树开始的标注
- 5. 丼例来说，语法的一个语法子集可以表示为下图所示。当给定一个句子 时，我们便可以按照从左到右的顺序来解析语法。例如，句子the man sleeps就可以表示为(S (NP (DT the) (NN man)) (VP sleeps))。
