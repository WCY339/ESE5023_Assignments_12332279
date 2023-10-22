#%% 导入matplotlib库
import matplotlib.pyplot as plt
#%% Find_expressions函数定义
def Find_expressions(num, target):
    res = []
    if not num:
        return res
    helper(res, num, target, "", 0, 0)
    return res
#%% 辅助函数定义
def helper(res, num, target, path, pos, eval):
    if pos == len(num):  # 如果已经遍历完所有数字
        if target == eval:  # 如果当前求和等于目标值
            res.append(path)  # 将表达式添加到结果列表中
        return
    for i in range(pos, len(num)):
        if i != pos and num[pos] == '0':  # 如果当前数字以0开头，则跳出循环
            break
        cur = num[pos:i+1]  # 获取当前数字的字符串形式
        if pos == 0:  # 如果是第一个数字
            helper(res, num, target, path+cur, i+1, int(cur))  # 继续向下递归，更新路径和求和结果
        else:
            helper(res, num, target, path+"+"+cur, i+1, eval+int(cur))  # 添加加号，继续向下递归，更新路径和求和结果
            helper(res, num, target, path+"-"+cur, i+1, eval-int(cur))  # 添加减号，继续向下递归，更新路径和求和结果

num = "123456789"
target = 50 # change this to your target value
solutions = Find_expressions(num, target)
print("Total solutions: ", len(solutions))
for solution in solutions:
    print(solution + f'={target}')

#%% 绘制Total_solutions列表
Total_solutions = []
for i in range(1, 101):
    expressions= Find_expressions(num, i)
    Total_solutions.append(len(expressions))

#%% 绘制折线图
plt.plot(range(1, 101), Total_solutions, color=(39/255, 93/255, 245/255), linestyle='-', linewidth=3)

# 添加标题和坐标轴标签
plt.title('Total Solutions for Integer i from 1 to 100')
plt.xlabel('Integer i')
plt.ylabel('Total Solutions')

# 设置坐标轴范围
plt.xlim(1, 100)
plt.ylim(min(Total_solutions), max(Total_solutions))

# 显示图例
plt.legend(['Total Solutions'])

# 显示网格线
plt.grid(True)

# 显示图形
plt.show()

#%% 找出产生的最大和最小值
max_solution = max(Total_solutions)
min_solution = min(Total_solutions)
print("产生最大值的数字是：",max_solution)
print("产生最小值的数字是：",min_solution)
