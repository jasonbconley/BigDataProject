import csv

# Both are CSV files. I imported all of the columns so that we could decide which are unnecessary
CDCDataset = open(r"C:\Users\eyon135\Documents\GitHub\Big-Data-Project\CDCDatasetCSV.csv", 'rt')
CDCreader = csv.reader(CDCDataset)
header = next(CDCreader)
print(header) # prints the column names

incomeDataset = open(r"C:\Users\eyon135\Documents\GitHub\Big-Data-Project\IncomeDataset.csv", 'rt')
incomereader = csv.reader(incomeDataset)
header = next(incomereader)
print(header) # prints the column names



# Below should work for pandas
#import pandas as pd

#CDCDataset = pd.read_csv(r'C:\Users\eyon135\Documents\GitHub\Big-Data-Project\CDCDatasetCSV.csv')
#CDCDataFrame = pd.DataFrame(CDCDataset, columns = ['res_state','res_county']) #just chose two columns
#print(CDCDataFrame) # to test printing out their names

#incomeDataset = pd.read_csv(r'C:\Users\eyon135\Documents\GitHub\Big-Data-Project\IncomeDataset.csv')
#incomeDataFrame = pd.DataFrame(incomeDataset, columns = ['State_ab','County']) #just chose two columns
#print(incomeDataFrame) # to test printing out their names
