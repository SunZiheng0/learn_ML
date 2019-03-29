from numpy import *

def standRegress(xArr, yArr):
    xMat = mat(xArr);
    yMat = mat(yArr).T;
    xTx = xMat.T * xMat;
    if(linalg.det(xTx) == 0):
        print("xTx has no inverse")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

def predict(xMat, ws):
    # return y_predict = X * ws
    return xMat * ws

