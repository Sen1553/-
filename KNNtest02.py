# -*- coding: UTF-8 -*-
import numpy as np
def file2matrix(filename):
    fr=open(filename)
    #打开文件
    arrayOLines = fr.readlines()
    #读取文件的所有行，并返回列表
    numberOfLines = len(arrayOLines)
    #len获得列表的行数
    returnMat =np.zeros((numberOfLines, 3))
    #np.zeros()生成并返回一个numberOfLines行，3列元素都为0的数组 3列的原因是给定的数据有三列特征
    classLabelVector = []
    #返回各数据的标签
    index = 0
    #行的索引值
    for line in arrayOLines:
        # 从0开始输出直到arrayOLines-1
        line = line.strip()
        #除去每行数据的首尾空格
        listFromLine = line.split('\t')
        #将字符串按\t分割
        returnMat[index, :] = listFromLine[0:3]
        #不是很清楚[index, :]，只理解提取前三列构成新的数组，把txt文件含标签的那列去掉
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        index += 1
    return returnMat, classLabelVector
        #list[-1]是读取列表倒数第一列
        #elif相当于 else if
        #didntLike设为1，smallDoses设为2，largeDoses设为3
        #list.append（xxx）会在列表后面加上字符‘xxx’

        

if __name__ == '__main__':
    filename = "datingTestSet.txt"
    #给定的数据集
    datingDataMat, datingLabels = file2matrix(filename)
    #分离矩阵和标签
    print(datingDataMat)
    print(datingLabels)



