import os
from rtree import index #Requires 'pip install rtree'
import pandas as pd

#Setup:
#Load Tree from file
prop = index.Property()
prop.dimension = 3
prop.dat_extension = 'data'
prop.idx_extension = 'index'
tree = index.Index('covid_data', properties=prop)
data = pd.read_csv('./processed_data.csv', encoding = "ISO-8859-1")
#Boundaries:
absoluteMinX, absoluteMinY, absoluteMinZ, absoluteMaxX, absoluteMaxY, absoluteMaxZ = tree.get_bounds()

#Manual Query:
#minX = 0 #fips
#maxX = 0
#minY = 0 #case count
#maxY = 0
#minZ = 0 #income
#maxZ = 0
#print(list(tree.intersection((absoluteMinX, absoluteMinY, absoluteMinZ, absoluteMaxX, absoluteMaxY, absoluteMaxZ))))

#From here, can print results based on:
#Where id == the id of the element found
# data['id'== foundID]

#Query as a Function:
def queryTheTree(minX = absoluteMinX, minY = absoluteMinY, minZ = absoluteMinZ, maxX = absoluteMaxX, maxY = absoluteMaxY, maxZ = absoluteMaxZ):
    inRange = list(tree.intersection((minX, minY, minZ, maxX, maxY, maxZ)))
    xVals = [] # Income
    yVals = [] # Case Count
    zVals = [] # County Name
    for val in inRange:
        xVals.append(data[data.id== val].iloc[0].average_income)
        yVals.append(data[data.id== val].iloc[0].case_count)
        zVals.append(data[data.id== val].iloc[0].county_name)
    return xVals, yVals, zVals
queryTheTree()
