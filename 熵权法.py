import heapq
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

stu = [['学生1',90,90,96],['学生2',76,93,84],['学生3',92,91,96],['学生4',98,76,90],['学生5',78,91,95],['学生6',70,91,92],
       ['学生7',98,81,76],['学生8',88,78,91],['学生9',71,73,77],['学生10',97,88,93],['学生11',67,72,89],['学生12',87,91,86],
      ['学生13',88,92,87],['学生14',77,80,86],['学生15',81,91,97],['学生16',72,85,91],['学生17',77,76,82],['学生18',77,91,82],
      ['学生19',88,56,76],['学生20',87,81,82],['学生21',81,77,62],['学生22',83,72,96],['学生23',80,93,91],['学生24',80,89,78]]
stu = pd.DataFrame(stu); stu.columns = ['name','project1','project2','project3']; stu.index = stu['name']; stu = stu[stu.columns[1:]]
# 01标准化处理
scaler = MinMaxScaler()
stu[['project1','project2','project3']] = scaler.fit_transform(stu[['project1','project2','project3']])
# 计算熵值和权重
yij = stu.apply(lambda x: x / x.sum(), axis=0)
K = 1/np.log(len(stu))     # 常数
tmp = yij * np.log(yij)
tmp = np.nan_to_num(tmp)
ej = -K * (tmp.sum(axis=0))       # 计算第j个指标的信息熵
wj = (1 - ej) / np.sum(1 - ej)        # 计算第j个指标的权重
score = yij.apply(lambda x: np.sum(100 * x * wj), axis=1)
top5 = heapq.nlargest(5, score)
print(score)