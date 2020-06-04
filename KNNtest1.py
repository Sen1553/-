# -*- coding: UTF-8 -*-
#使py文件支持中文

import numpy as np
import operator

# group--样本集   labels--标签
# group为四行两列，四个样本，两个特征，特征分别为电影的打斗次数和接吻次数
def createDataSet():
    group= np.array([[1,101],[5,89],[108,5],[115,8]])
    labels= ['爱情片', '爱情片', '动作片', '动作片']
    return group, labels

# KNN算法 分类器
# inX 待测试的数据 dataSet样本集 labels样本标签 k 取k个近邻的数
def classify(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    # shape函数会返回矩阵的行数和列数 shape[0]返回行数    shape[1]返回列数
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat ** 2

    # np.tile函数会按照某些方向复制元素  np.tile([101,20],(4,1))会将[101,20]沿y轴复制四倍，沿x轴复制一倍
    """
    沿y轴复制的倍数是样本个数
    设inX为[101,20]结果如下
    [[101,20]
    [101,20]
    [101,20]
    [101,20]]
    """
    # np.tile(inX,(dataSetSize,1))-dataSet是将测试数据的矩阵与样本数据作差，为计算欧式距离做铺垫

    # **是幂运算  分别计算两个特征差值的平方
    sqDistances = sqDiffMat.sum(axis=1)
    # axis是轴的意思
    """
    sum()将元素相加，sum（0）沿列相加，sum(1)沿行相加
    使用0值表示沿着每一列或行标签索引值向下执行方法
    使用1值表示沿着每一行或者列标签模向执行对应的方法
    这里要计算测试数据与样本数据的距离，故使用sum(1)行相加
    """
    distances = sqDistances**0.5
    # 开根号即得测试数据与每一个样本的欧式距离

    sortedDistIndices = distances.argsort()
    # argsort会将distances中的数据从小到大排序，返回该数据对应的位次 数据从0开始
    """
        [12 24 8 30]
    位置 0  1  2  3
    返回  [2 0 1 3] 升序排列
    """
    classCount = {}
    # 创建字典记录标签次数

    # for i in range(k)----从0开始输出直到k-1
    # range(起始值，终止值，步长)
    """ 
    for i in range （1，3）：
       从1开始到3-1结束就是把1,2依次赋值给i
    """
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # dict.get(key, default=None)key -- 字典中要查找的键   default -- 如果指定键的值不存在时，返回该默认值。
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
    #返回出现频率最高的标签，做为该测试数据的标签


    """
     items() 方法以列表返回可遍历的(键, 值) 元组数组----[(’爱情片‘，2),(‘动作片’，1)]
     [0][0]为最大频率的标签
    key=operator.itemgetter(1)根据字典的值进行排序
                key=operator.itemgetter(0)根据字典的键进行排序
                reverse降序排序字典
    
    """

if __name__ == '__main__':
    #创建数据集
    group, labels = createDataSet()
    #测试集
    test = [8,110]
    #kNN分类
    test_class = classify(test,group,labels,3)
    #打印分类结果
    print(test_class)

