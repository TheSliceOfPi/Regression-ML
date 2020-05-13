import sys
import os
import subprocess

def main():
    originalFileName=sys.argv[1]
    originalFile=open(originalFileName,"r")
    originalLine=originalFile.readline()
    totalLines=0
    #Counting number of samples
    while originalLine:
        totalLines=totalLines+1
        originalLine=originalFile.readline()
    originalFile.close()
    sectSize=totalLines//5
    avgFile=open("avgLosses.txt","w+")
    avgArray=[0]*10
    for i in range(5):
        avgFile.write("%Subfold "+str(i)+'\n')
        trainingFile=open("training.txt","w+")
        testFile=open("test.txt","w+")
        total=0
        originalFile=open(originalFileName,"r")
        line=originalFile.readline()
        for j in range(i*(sectSize+1)):
            trainingFile.write(line)
            line=originalFile.readline()
        for j in range(sectSize+1):
            total=total+1
            testFile.write(line)
            line=originalFile.readline()
        while line:
            trainingFile.write(line)
            line=originalFile.readline()
        originalFile.close()
        trainingFile.close()
        testFile.close()
        
        #Regression calculation STARTS
        for j in range(1,11):
            avgFile.write(str(j)+' ')
            subprocess.call("python3 reg.py training.txt test.txt "+str(j)+' > ./output.txt' , shell=True)
            outputFile=open("output.txt","r")
            line=outputFile.readline()
            while line:
                if ("Average" in line):
                    line=line.split()
                    avgFile.write(line[-1]+'\n')
                    avgArray[j-1]=avgArray[j-1]+float(line[-1])
                line=outputFile.readline()
            outputFile.close()
        avgFile.write('\n')
    avgFile.write("Overall Averages: \n")
    
    for i in range(len(avgArray)):
        avgFile.write("Degree "+ str(i+1)+": "+str(avgArray[i]/5)+"\n")
    avgFile.write("\n")
    avgFile.write("Min of Overall Averages: "+str(min(avgArray)/5)+"\n")
    avgFile.close()
            
            
            
            
        #Regression calculation ENDS
        
            

main()
