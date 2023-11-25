import numpy as np
list=[np.array([3,2,8,9]),np.array([4,12,34,25,78]),np.array([23,12,67])]
mean_List=[]
#use a for loop to iterate through each array in the list
for i in list:
  arr1 = i
  mean=np.mean(i) #calculate mean

  mean_List.append(mean) #append the mean value

print("Mean of every array:",mean_List) #print the value
#output
#Mean of every array: [5.5, 30.6, 34.0]
