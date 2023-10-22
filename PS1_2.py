# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:17:11 2023

@author: 401
"""
#%% 导入numpy库
import numpy as np
#%% 生成矩阵
M1 = np.random.randint(0, 50, [5, 10])
M2 = np.random.randint(0, 50, [10, 5])
print("5行10列的矩阵M1是：",M1)
print("10行5列的矩阵M2是：",M2)
#%% 定义矩阵乘法函数
def Matrix_multip(M1, M2):
    M = np.zeros((5, 5))
    for i in range(5):
      for j in range(5):
         M[i, j] = sum(M1[i, :] * M2[:, j])
    return M     
#%% 计算矩阵乘法并验证结果
M = Matrix_multip(M1, M2)
M3 = np.dot(M1, M2)  
# 判断M与M3是否相等
if np.array_equal(M, M3):
    print("经验证M与M3相等,矩阵乘法函数编写正确")
else:
    print("经验证M与M3不相等，矩阵乘法函数编写错误")

