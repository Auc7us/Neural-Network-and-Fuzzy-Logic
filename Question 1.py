import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D  

loc = (r'D:\CMS 3-1\NNFL\Assignment\As-1\data.xlsx')
wb = xl.open_workbook(loc)
sheet = wb.sheet_by_index(0)
lRate = 0.000000001#random learning rate
ncols = sheet.ncols
#print('ncols',ncols)
nrows = sheet.nrows
#print('nrows',nrows)
temp1 = np.array([sheet.col_values(0)])
weight = np.ones((10*nrows,ncols-1), dtype=float )
 
weight[0,0] = 0
weight[0,1] = 0
#print(type(weight))


#Making a 2D-array of given data 
for i in range(1,ncols,1):
  k = np.array([sheet.col_values(i)])
  ar = np.concatenate((temp1,k))
  temp1 = ar
  print('\n\n\n')
  
print(ar)  
newArray = np.transpose(ar) 
print('\n\n\n new array begins\n',newArray,'\n newarrayends\n\n\n')
#print('newarray[0,0]',newArray[0,0],'\n')
#print('weight[0,0]',weight[0,0],'\n\n\n')
#print('newarray[0,1]',newArray[0,1],'\n')
#print('weight[0,1]',weight[0,1],'\n\n\n')
#required functions
# n = number of feature vectors/samples
# j = number of sample
# i = number of iteration-1
def predValue(j,i):
  Sum = 0
  for n in range(ncols-1):
    #print('the value of n in predvalue is ', n,'\n\n' )
    newValue = (newArray[j,n])*(weight[i,n])
    Sum = newValue + Sum 
  return Sum

def costFunction(i):
  temp = 0
  for j in range(nrows-1):
    error = (predValue(j,i)) - (newArray[j,2])
    costFuncPI = 0.5*error*error
    costFunc = costFuncPI + temp
    temp = costFunc
  
  return costFunc

def weightUpdate(i):
  temp = 0
  for n in range(ncols-1):
    #print ('value of n is ',n,'\n\n')
    for j in range(nrows-1):
      error = (predValue(j,i)) - (newArray[j,2])
      minCostFuncPI = (error)*newArray[j,n]
      summedError = minCostFuncPI + temp
      temp = summedError      
    #print('summed error is',summedError)
    weight[i+1,n] = weight[i,n]-lRate*(summedError)
    #print('i and n respectively are ',i,' ',n,'\n\n')
    #print('the weight requested is ',weight[i,n],'    ',weight[i+1,n])
    
# Main


print('\n\n\n\nPlease specify the number of inputs to be given')
userInput = input()
print('\n\n\n')

k = int(userInput)

costFuncArray = np.zeros((k), dtype = float)
nIterations = np.zeros((k), dtype = float)
weightArray1 = np.zeros((k), dtype=float )
weightArray2 = np.zeros((k), dtype=float )
for i in range(k):
  Result = costFunction(i)
  weightUpdate(i)
  costFuncArray[i] = Result
  nIterations[i] = i
  print('The value of Cost Function after iteration#',i+1,'is',Result)
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
#print(Result)
#Result = costFunction(0)
#print('predictedvalue is',predValue(0,0))