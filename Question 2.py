
import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

loc = (r'D:\CMS 3-1\NNFL\Assignment\As-1\data.xlsx')
wb = xl.open_workbook(loc)
sheet = wb.sheet_by_index(0)
lRate = 0.000001  #takes 5 iterations
#lRate = 0.0000001 #takes ~100 iterations
ncols = sheet.ncols
nrows = sheet.nrows
temp1 = np.array([sheet.col_values(0)])
weight = np.ones((10*nrows,ncols-1), dtype = float)
weight[0,0] = 0
weight[0,1] = 0

for i in range(1,ncols,1):
  k = np.array([sheet.col_values(i)])
  ar = np.concatenate((temp1,k))
  temp1= ar
print('\n\n\n')
print(ar)
newArray = np.transpose(ar)
print('\n\nthe array being used is\n',newArray,'\n')

def predValue(j,i):
  Sum = 0
  for n in range(ncols-1):
    newValue = (newArray[j,n])*(weight[i,n])
    Sum = newValue + Sum
  return Sum

def costFunction(i):
  temp = 0
  for j in range(nrows-1):
    error = (predValue(j,i)) - (newArray[j,2])
    costFuncPI = 0.5*error*error 
    costFunc= costFuncPI + temp
    temp= costFunc
    
  return costFunc

def weightUpdate(i):
  for n in range(ncols-1):
    for j in range(nrows-1):
      error = (predValue(j,i)) - (newArray[j,2])
      minCostFuncPI = error*newArray[j,n]
    weight[i+1,n] = weight[i,n] - lRate*(minCostFuncPI)
    
#main
print('\n\nplease specify the number of iterations')
userInput = input()
k = int(userInput)

costFuncArray = np.zeros((k), dtype = float)
nIterations = np.zeros((k), dtype = float)
weightArray1 = np.zeros((k), dtype = float)
weightArray2 = np.zeros((k), dtype  = float)
for i in range(k):
  result = costFunction(i)
  weightUpdate(i)
  costFuncArray[i] = result
  nIterations[i] = i
  print('The value of cost function after iteration#',i+1,'is',result)
print('weight1=',weight[i,0],'weight2=' ,weight[i,1])
#Graph1(2D)
plt.plot(nIterations,costFuncArray, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=5)
plt.xlabel('number of iterations')
plt.ylabel('cost function')
plt.title('cF vs i')
plt.show()

for i in range(k):
  weightArray1[i] = weight[i,0]
  weightArray2[i] = weight[i,1]

#Graph2(3D)
fig = plt.figure()
ax = plt.axes(projection="3d")
zLine = costFuncArray
xLine = weightArray1
yLine = weightArray2
ax.plot3D(xLine, yLine, zLine, 'gray')    
    