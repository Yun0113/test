# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
ratings = pd.read_csv('D:\ChromeCoreDownloads\ml-latest-small/ratings.csv',index_col=None)#读取数据
rating_mean = ratings.groupby(['movieId'],as_index=False)['rating'].mean()#按照电影ID进行分组
rating_mean.columns = ['movieId','rating_mean']#列名重命名

# 使用apply函数, 添加comment列，如果字段rating>4，则'判断'这一列赋值为'推荐',否则为‘不推荐’
rating_mean['comment'] = rating_mean.rating_mean.apply(lambda x:'推荐' if x > 4 else '不推荐')#添加一个comment列
comment = ratings.merge(rating_mean, left_on='movieId', right_on='movieId')
comment = comment.drop(['rating_mean'], axis=1)
comment = comment.sort_values(['userId'])#按照客户ID进行排序
comment.to_csv('E:/comment.csv')#输出到一个comment.csv中