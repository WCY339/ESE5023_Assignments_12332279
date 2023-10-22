# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:40:57 2023

@author: 401
"""
#%% 定义生成帕斯卡三角形的函数
def Pascal_triangle(k):
    # 初始化帕斯卡三角形列表
    Pascal_triangle=[]
    for i in range(k):
       row = [1]*(i + 1) 
       # 当行数大于等于2时，利用帕斯卡三角形的性质进行计算
       if i >= 2: 
         for j in range(1,i): 
            # 当前元素等于上一行的前一个元素和上一行的当前元素的和
            row[j] = Pascal_triangle[i-1][j-1] + Pascal_triangle[i-1][j]
       # 将当前行添加到帕斯卡三角形列表中
       Pascal_triangle.append(row)  
    # 返回帕斯卡三角形列表
    return Pascal_triangle 

#%% 定义打印帕斯卡三角形的函数
def Print_Pascal_triangle(Pascal_triangle):
    # 对于帕斯卡三角形中的每一行
    for row in Pascal_triangle:
        # 打印当前行的所有元素，元素之间用空格隔开
        print(' '.join(str(num) for num in row))

#%% 生成帕斯卡三角形
Pascal_triangle20 = Pascal_triangle(20)
Pascal_triangle100 = Pascal_triangle(100)
Pascal_triangle200 = Pascal_triangle(200)
# 打印帕斯卡三角形
Print_Pascal_triangle(Pascal_triangle20) 
Print_Pascal_triangle(Pascal_triangle100)   
Print_Pascal_triangle(Pascal_triangle200) 

