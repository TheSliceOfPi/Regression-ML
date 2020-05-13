Edith Flores
Homework 2: Regression-Least

Files Submitted:
reg.py
fiveFold.py
synthdata.txt
syn_train.txt
syn_validation.txt
training.txt
test.txt
output.txt
avgLosses.txt
Homework Cover Sheet ML-2.pdf
MLHW2.Report.pdf
readme.txt

--------reg.py-----------------
The program reg.py takes a file with the training samples, and a file with the validation samples. Both of these files are set up such that the first number in each row is the input, and the second number in the row is the output.  Reg read each sample in the training set and creates the weighted matrix, W, using the equation W=(((X^T)*X)^-1)*(X^T)*t. Once the Weighted matrix is calculated, the final function is created and printed on the command line.Once this is done, Reg reads each of the validation sample's input and plugs it into the function. The ouput is our prediction. Reg then finds the avg loss by finding the sum of all the losses ((t-prediction)**2) and dividing by the number of samples. Reg prints the avg loss and prints out the validation samples real input/output and the curve of the function.
To run for homework: python3 reg.py syn_train.txt syn_validation.txt <Poly degrre>
To run(general): python3 reg.py <training set filename> <validation set filename> <poly degree >

--------fiveFold.py--------------
The program fiveFold.py takes a data file where the first number in each row is the input and the second number in each row is the output. fiveFold takes the file and does five-fold cross-validation by creating a training file with 4/5 od the total data, and a testing file with 1/5 of the total data. Everytime the file is split, the program calls reg.py to determine the function and avg loss at n=1 to 10 and write it on to an output file, avgLosses.txt, that keeps track of every avg loss calculated.

To run for homework: python3 fiveFold.py synthdata.txt
To run (general): python3 fiveFold.py <data file's name> 

