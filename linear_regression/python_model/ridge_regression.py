from numpy import *;

def redgeRegress(xMat, yMat, lamda=0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lamda
    ws = denom.I * (xMat.T * yMat)
    return ws
