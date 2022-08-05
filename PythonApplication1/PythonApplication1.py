#Rajeshwor Niroula
#transactions to bool Matrix
import re
import numpy as np
import pandas as pd 

#reading lines from dataset ie no of rows
with open('grocery_dataset.txt') as f:
    lines = f.readlines()
transactions = len(lines)

#extracting total item list ie no of columns  
itemList = []
for x in lines:
    line = re.split(",|\\n",x)
    for y in line:
        if y != "":
            if y not in itemList:
                 itemList.append(y)
itemNum = len(itemList)

#creating transactions * itemNum matrix initialized as zero
matrix = np.zeros((transactions,itemNum),dtype=bool)
row = 0
column = 0

#compairing transactions with itemlist and filling matrix
for x in lines:
    line = re.split(",|\\n",x)
    for y in line:
        if (row == transactions):
            break
        if y in itemList:
            column = itemList.index(y)
            matrix[row][column] = 1
    row = row + 1

#saving result to file.csv (readable in visual studio)
stackedMatrix = np.row_stack((itemList,matrix))
print(stackedMatrix)
print("output too big for console, open out.txt in vs. Note gorcery_dataset.txt has to be in the same directory for the program to work")
pd.DataFrame(stackedMatrix).to_csv("file.csv",header=False,index=False)

