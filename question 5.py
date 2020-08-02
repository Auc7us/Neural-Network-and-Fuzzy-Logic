

import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

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
for i in range(1,ncols-1,1):
  k = np.array([sheet.col_values(i)])
  ar = np.concatenate((temp1,k))
  temp1 = ar
  print('\n\n\n')

  
  
  
  
#print(ar)  
arrayX = np.transpose(ar) 
#print('\n\n\n new array begins\n',arrayX,'\n newarrayends\n\n\n')
arrayY = np.transpose(np.array([sheet.col_values(0)]))
#print(arrayY)
transX = np.transpose(arrayX)
reqMultX = np.dot(transX,arrayX)
reqInvMat = np.linalg.inv(reqMultX)
reqMultY = np.dot(transX,arrayY)
weight = np.dot(reqMultX,reqMultY)
print(weight)
#finMatX = np.dot(reqInvMat,transX)
 
'''
weight2 = np.dot(finMatX[1,:],arrayY)
print(weight1)
print(weight2)
'''     