# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
ratings = pd.read_csv('D:\ChromeCoreDownloads\ml-latest-small/ratings.csv',index_col=None)#读取数据
rating_count = ratings.groupby(['rating'],as_index=False)['movieId'].count()#按照评分进行分组
rating_count.columns = ['rating','movieId_count']#列名重命名       
rating_interval = {'(0,1]分段电影数': 0,'(1,2]分段电影数': 0,'(2,3]分段电影数': 0,'(3,4]分段电影数':0,'(4,5]分段电影数': 0}#创建分段字典     
for i in range(0,len(rating_count)):
    if 0<rating_count.rating[i]<=1:
        rating_interval['(0,1]分段电影数'] += rating_count.movieId_count[i]
for i in range(0,len(rating_count)):
    if 1<rating_count.rating[i]<=2:
        rating_interval['(1,2]分段电影数'] += rating_count.movieId_count[i]
for i in range(0,len(rating_count)):
    if 2<rating_count.rating[i]<=3:        
        rating_interval['(2,3]分段电影数'] += rating_count.movieId_count[i]
for i in range(0,len(rating_count)):
    if 3<rating_count.rating[i]<=4:    
        rating_interval['(3,4]分段电影数'] += rating_count.movieId_count[i]
for i in range(0,len(rating_count)):
    if 4<rating_count.rating[i]<=5:    
        rating_interval['(4,5]分段电影数'] += rating_count.movieId_count[i]

rating_count = pd.DataFrame.from_dict(rating_interval,orient='index')
print(rating_count)

        