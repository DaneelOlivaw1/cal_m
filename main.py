import pandas as pd
import time

# 数据读入
a = pd.read_excel("a.xlsx")
b = pd.read_excel("b.xlsx")

# 数组初始化赋值
t = [[0 for i in range(10)] for i in range(10)]
m = [[0 for i in range(10)] for i in range(10)]
o = [[0 for i in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        m[i][j] = a.iat[i, j]
        o[i][j] = b.iat[i, j]

# 每次的计算函数
def cal():
    for i in range(9):
        for j in range(9):
            x = o[i][9] / m[i][9]
            y = o[9][j] / m[9][j]
            t[i][j] = (x + y) / 2
            
    for i in range(9):
        for j in range(9):
            m[i][j] = m[i][j] * t[i][j]

    for i in range(9):
        summ = 0
        for j in range(9):
            summ = summ + m[i][j]
        m[i][9] = summ

    for j in range(9):
        summ = 0
        for i in range(9):
            summ = summ + m[i][j]
        m[9][j] = summ

# 检测误差
def cmp():
    for i in range(9):
        rate = abs(m[9][i] - o[9][i]) / o[9][i]
        print(rate)
        if rate > 0.01:
            return True
    
    for i in range(8):
        rate = abs(m[i][9] - o[i][9]) / o[i][9]
        print(rate)
        if rate > 0.01:
            return True
    return False

cnt = 1
while(cmp()):
    print(cnt)
    cal()
    cnt += 1
    
    time.sleep(1)

for i in m:
    print(i)

