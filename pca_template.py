
# coding: utf-8




from numpy import *
from matplotlib import pyplot as plt
import sys


def loadDataSet(fileName = 'iris_with_cluster.csv'):
    dataMat=[]
    labelMat=[]
    fr = open(fileName)
    for line in fr.readlines():
        lineArray=line.strip().split(',')
        records = []
        for attr in lineArray[:-1]:
            records.append(float(attr))
        dataMat.append(records)
        labelMat.append(int(lineArray[-1]))
    dataMat = array(dataMat)
    
    labelMat = array(labelMat)
    
    
    return dataMat,labelMat

def pca(dataMat, PC_num=2):
    '''
    Input:
        dataMat: obtained from the loadDataSet function, each row represents an observation
                 and each column represents an attribute
        PC_num:  The number of desired dimensions after applyting PCA. In this project keep it to 2.
    Output:
        lowDDataMat: the 2-d data after PCA transformation
    '''

    X = array(dataMat, dtype=float)
    X_centered = X - X.mean(axis=0)
    covariances = cov(X_centered, rowvar=False)

    eigVals, eigVecs = linalg.eigh(covariances)
    # print("Eigenvalues:\n", eigVals)
    # print("Eigenvectors:\n", eigVecs)

    sort_idx = argsort(eigVals)[::-1]
    eigVec_sorted = eigVecs[:, sort_idx]
    W = -eigVec_sorted[:, :PC_num]

    lowDDataMat =  X_centered @ W

    return array(lowDDataMat)


def plot(lowDDataMat, labelMat, figname):
    '''
    Input:
        lowDDataMat: the 2-d data after PCA transformation obtained from pca function
        labelMat: the corresponding label of each observation obtained from loadData
    '''

    
    lowDDataMat = array(lowDDataMat)
    labelMat = array(labelMat)

    plt.figure(figsize=(6.5, 5.0), dpi=120)
    
    labels = unique(labelMat)
    cmap = plt.get_cmap('tab10')
    colors = {lbl: cmap(i % 10) for i, lbl in enumerate(labels)}

    for lbl in labels:
        idx = labelMat == lbl
        plt.scatter(lowDDataMat[idx, 0], lowDDataMat[idx, 1], s=25, c=[colors[lbl]])

    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA')
    plt.tight_layout()
    plt.savefig(figname)
    plt.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'iris_with_cluster.csv'
    figname = filename
    figname = figname.replace('csv','jpg')
    dataMat, labelMat = loadDataSet(filename)
    
    lowDDataMat = pca(dataMat)
    
    plot(lowDDataMat, labelMat, figname)
    

