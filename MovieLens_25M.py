# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
ratings = pd.read_csv('D:\ChromeCoreDownloads\ml-25m/ratings.csv',index_col=None)#读取数据
movies = pd.read_csv('D:\ChromeCoreDownloads\ml-25m/movies.csv',index_col=None)#读取数据
tags = pd.read_csv('D:\ChromeCoreDownloads\ml-25m/tags.csv',index_col=None)#读取数据

userid = ratings.drop_duplicates(subset='userId',keep='first',inplace=False)#去除重复的用户名
userid_count = userid.shape[0] #不同用户名的数量
print("不同用户名的数量:%s"%(userid_count))

movieid = movies.drop_duplicates(subset='movieId',keep='first',inplace=False)#去除重复的电影名
movieid_count = movieid.shape[0] #不同电影名的数量
print("不同电影名的数量:%s"%(movieid_count))

genres = movies.drop_duplicates(subset='genres',keep='first',inplace=False)#去除
genres_count = genres.shape[0] #电影的种类类别
genres_types = genres.genres
codes = []
for genres_type in genres_types:
   codes.append(genres_type)
#print(codes)
#len(codes)
genres1 = []
for i in range(0,len(codes)):
    code = codes[i]
    code_split = code.split('|')
    for j in range(0,len(code_split)):
        genres1.append(code_split[j])        
#len(set(genres1))
print("电影类别数量:%s"%(len(set(genres1))))#电影类别数量



    
    
    

