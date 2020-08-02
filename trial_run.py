
import xlrd as xl
import numpy as np


loc = (r'D:\CMS 3-1\NNFL\Assignment\As-1\data.xlsx')
wb = xl.open_workbook(loc)
sheet = wb.sheet_by_index(0)
lRate = 0.01 #random learning rate

ncols = sheet.ncols
print('ncols',ncols)
nrows = sheet.nrows
print('nrows',nrows)
temp1 = np.array([sheet.col_values(0)])
k = 10 #random number of iterations
weight = np.ones((nrows,ncols-1), dtype=float )
weight[0,0] = 5.01
weight[0,1] = 6.020

print(type(weight))

print(weight)

#Making a 2D-array of given data 
for i in range(1,ncols,1):
  k = np.array([sheet.col_values(i)])
  ar = np.concatenate((temp1,k))
  temp1 = ar
  print('\n\n\n')
  
print(ar)  
newArray = np.transpose(ar) 
print('\n\n\n new array begins\n',newArray,'\nnewarrayends\n\n\n')
print('newarray[0,0]',newArray[0,0],'\n')
print('weight[0,0]',weight[0,0],'\n\n\n')
print('newarray[0,1]',newArray[0,1],'\n')
print('weight[0,1]',weight[0,1],'\n\n\n')
#required functions
# n = number of feature vectors/samples
# j = number of sample
# i = number of iteration-1
def predValue(j,i):
  Sum = 0
  
  for n in range(ncols-1):
    newValue = (newArray[j,n])*(weight[i,n])
    Sum = newValue + Sum 
 
  return Sum

def costFunction(i):
  temp = 0
  for j in range(0,nrows-1,1):
    error = (predValue(j,i)) - (newArray[j,2])
    costFuncPI = 0.5*error*error
    costFunc = costFuncPI + temp
    temp = costFunc
    weightUpdate(i)
  return costFunc

def weightUpdate(i):
  temp = 0
  for n in range(0,ncols-2,1):
    for j in range(0,nrows-1,1):
      error = (predValue(j,i)) - (newArray[j,2])
      minCostFuncPI = (error)*newArray[j,n]
      summedError = minCostFuncPI + temp
      temp = summedError      
    weight[i+1,n] = weight[i,n]-lRate*(summedError)

for i in range(10):
  Result = costFunction(i)
  print('The value of Cost Function after iteration#',i,'is',Result)

#Result = costFunction(0)
#print(Result)
#print('predictedvalue is',predValue(0,0))