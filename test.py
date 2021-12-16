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
# 开始循环💩
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
    # print(emotion)
    # print(mark)
    # print(" ")
    print("已成功输出第"+str(i+1)+"行文件！")

# 关闭文件
output.close()
# 汇报结果
print("本次共输出"+str(i+1)+"行数据，全部操作完成！")