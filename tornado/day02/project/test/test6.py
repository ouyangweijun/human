import pandas as pd

csv_data = pd.read_csv('wandoujia_app_cat.csv')  # 读取训练数据
# print(csv_data.shape)  # (189, 9)
# N = 1
# csv_batch_data = csv_data.tail(N)  # 取后5条数据
# print(csv_batch_data.shape)  # (5, 9)
# train_batch_data = csv_batch_data[list(range(3, 6))]  # 取这20条数据的3到5列值(索引从0开始)
# print(train_batch_data)
#

#print(csv_data.head())

from decimal import Decimal
from decimal import getcontext

mb =[]
kb =[]
for i in csv_data['软件大小']:
    # print(type(i),'你%s好' % i)
    if i.endswith('MB'):
        mb.append(i)
        # print(i)
    if i.endswith('KB'):
        kb.append(i)
mbsum = 0.00
for j in mb:
    a = j.split("MB")[0]
    #print(type(a))
    # print(type(float(a)))
    mbsum += float(a)
print("MB大小一共是%sMB" % mbsum)
kbsum = 0
for k in kb:
    b = k.split("KB")[0]
    kbsum +=int(b)
kb_mvb = kbsum / 1024
print("kb一共的安装包大小是%sMB" % kbsum)
result = mbsum + float(kb_mvb)
print("一共的安装包大小是%sMB" % result)
print("一共的安装包大小是%sGB" % (result/1024))
tb=result/1024/1024
print("一共的安装包大小是%sGB" % (tb))