# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
ratings = pd.read_csv('D:\ChromeCoreDownloads\ml-latest-small/ratings.csv',index_col=None)#读取数据
movies = pd.read_csv('D:\ChromeCoreDownloads\ml-latest-small/movies.csv',index_col=None)#读取数据
tags = pd.read_csv('D:\ChromeCoreDownloads\ml-latest-small/tags.csv',index_col=None)#读取数据

rating_mean = ratings.groupby(['movieId'],as_index=False)['rating'].mean()#按照电影ID进行分组
rating_mean.columns = ['movieId','rating_mean']#列名重命名
data = pd.merge(rating_mean,movies,on='movieId')
data = pd.merge(data,tags,on='movieId')
Movie_information = data[['title','rating_mean','tag']] 
Movie_information.to_csv('E:/Movie_information.csv')#输出到一个Movie_information.csv中