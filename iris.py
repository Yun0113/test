# -*- coding: utf-8 -*-
import pandas as pd
df_Iris = pd.read_csv('D:\ChromeCoreDownloads\data_basics-2020-7-23-2-19-53-38-master/Iris.csv')
#前5行
df_Iris.head()
#后5行
df_Iris.tail()
df_Iris.describe()
#分割
df_Iris['Name']= df_Iris.Name.apply(lambda x: x.split('-')[1])
df_Iris.Name.unique()
import seaborn as sns
import matplotlib.pyplot as plt
#sns初始化
sns.set()
#hue表示按照Name对数据进行分类, 而style表示每个类别的标签系列格式不一致.
#花萼的长度和宽度在散点图
sns.relplot(x='SepalLengthCm', y='SepalWidthCm', hue='Name', style='Name', data=df_Iris )
plt.title('SepalLengthCm and SepalWidthCm data by Name')
#花瓣长度与宽度分布散点图
sns.relplot(x='PetalLengthCm', y='PetalWidthCm', hue='Name', style='Name', data=df_Iris )
plt.title('PetalLengthCm and PetalWidthCm data by Name')
