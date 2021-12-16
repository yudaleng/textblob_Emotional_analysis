# 使用textblob进行句子情感分析

## 前期准备

### 安装textblob

textblob是python的一个开源处理库，它项目地址为：[https://github.com/sloria/TextBlob](https://github.com/sloria/TextBlob)

使用命令，进行安装

```
pip install textblob
```

### 安装pandas

pandas是python的一个处理数据的库，对于本项目来说，该库用于分割txt的语句。

使用命令，进行安装

```
pip install pandas
```

## 代码部分

```python
# 用于情感分析
from textblob import TextBlob
# 用于读取txt数据
import pandas as pd

# 读取文件
data = pd.read_table(r'test_x.txt', sep=',', header=None)
# 读取txt的第二列
line = data[1]
index = data[0]
# 打开准备写入的文件
output = open("text_y.txt", "w", encoding='utf-8')
output.write("index  lable"+'\n')
i = -1
# 开始循环
for single_line in line:
    i = i+1
    blob = TextBlob(single_line)
    line_index = index[i]
    # 进行分词分句处理
    blob.sentences
    # 开始情感分析
    mark = blob.sentences[0].sentiment.polarity
    # 判断情感等级
    if mark == 0:
        emotion = 'neutral'
    elif mark > 0:
        emotion = 'positive'
    elif mark < 0:
        emotion = 'negative'
    # 输出情感分析结果
    output.write(str(line_index)+"->"+emotion+"\n")
    print("已成功输出第"+str(i+1)+"行文件！")

# 关闭文件
output.close()
# 汇报结果
print("本次共输出"+str(i+1)+"行数据，全部操作完成！")
```

## 遇到的问题

在调用textblob时，可能会出现以下错误：

![image-20211216161536739](/Users/yuleng/Library/Application Support/typora-user-images/image-20211216161536739.png)

由于textblob会依赖于NLTK的一些东西，在运行程序时，由于电脑内并没有，便需要下载。由于在线安装不稳定，推荐去官网下载离线包进行安装。

包下载地址：[http://www.nltk.org/nltk_data/](http://www.nltk.org/nltk_data/)

将包文件解压至 ~python安装文件夹/nltk_data/tokenizers/ 即可安装



这里将项目文件打包至我的GitHub上，用于记录学习。
