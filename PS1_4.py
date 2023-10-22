# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:44:22 2023

@author: 401
"""
#%% 导入random库
import random

#%% 定义计算最少步数的函数
def Least_moves(x):
    moves=0
    while x>1:
         if x%2==0:
             x=x/2
             moves=moves+1
         else:
             x=x-1
             moves=moves+1
    return moves

#%%随机生成1到100之间的整数
x=random.randint(1, 100)
validation1=2
validation2=5
#%% 打印最少步数并验证1与5的最少步数结果
print("2的最少步数是：",Least_moves(validation1))
print("5的最少步数是：",Least_moves(validation2))
print("随机数x的最少步数是：",Least_moves(x))