import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from numpy import *
from numpy.linalg import *
import sys

def main():
    ##Training Regression STARTS
    trainingFileName=sys.argv[1]
    trainingFile=open(trainingFileName,"r")
    n=int(sys.argv[3])
    matX=[]
    t=[]
    axisX=[]
    #Reading each row to create matrix
    line=trainingFile.readline()
    while line:
        row=[]
        info=line.split()
        x=float(info[0])
        axisX.append(x)
        t.append(float(info[1]))
        for i in range(n+1):
            row.append(x**i)
        matX.append(row)
        line=trainingFile.readline()
    #Calculating the Weighted Matrix, W
    X=array(matX)
    t=array(t)
    # we will use the equation W =((X.T*X).I*X.T)*t.T
    W = dot(inv(dot(X.transpose(), X)), dot(X.transpose(), t.transpose()))
    func="f(x)="
    for i in range(n+1):
        if(i==0):
            func=func+str(W[i])+"+"
        elif(i==n):
            func=func+"("+str(W[i])+" x^"+str(i)+")"
        else:
            func=func+"("+str(W[i])+" x^"+str(i)+")"+"+"
    print(func)
    ##Training Regression ENDS
    
    ##Testing validation STARTS
    validationFileName=sys.argv[2]
    validationFile=open(validationFileName,"r")
    totalLines=0
    line=validationFile.readline()
    totalDiff=0
    validInp=[]
    actualOut=[]
    predOut=[]
    while line:
        totalLines=totalLines+1 #Keeps track of how many total predictions
        info=line.split()
        validInp.append(float(info[0]))
        actualOut.append(float(info[1]))
        pred=0 
        for i in range(n+1):
            pred=pred+(W[i]*(float(info[0])**i))
        predOut.append(pred)
        totalDiff=totalDiff+((float(info[1])-pred)**2)
        line=validationFile.readline()
    avgLoss=totalDiff/totalLines
    print("Average loss: ",avgLoss)
    ##Testing validation ENDS
    
    ##Plot points and curve STARTS
    validInp=array(validInp)
    predOut=array(predOut)
    actualOut=array(actualOut)
    xMin=amin(validInp)
    xMax= amax(validInp)
    yMin=amin(minimum(actualOut,predOut))
    yMax=amax(maximum(actualOut,predOut))
    
    #Curve calculations STARTS
    x=linspace(xMin, xMax, 10000)
    regX=ones((len(x), 1))
    for i in range(1,n+1):
        regX = column_stack((regX, power(x, i)))
    y=dot(regX,W)
    #Curve calculations ENDS
    
    plot.ion()
    plot.subplot(111)
    plot.plot(validInp,actualOut , 'go', markersize=3)
    plot.plot(x,y , '-b', markersize=1)
    plot.xlabel('Input')
    plot.ylabel('Output')
    plot.draw()
    input('<press enter>')
    ##Plot points and curve ENDS
    
main()
