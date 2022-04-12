import os
from rtree import index #Requires 'pip install rtree'

#Load Tree from file
prop = index.Property()
prop.dimension = 3
prop.dat_extension = 'data'
prop.idx_extension = 'index'
tree = index.Index('covid_data', properties=prop)
#Boundaries:
absoluteMinX, absoluteMinY, absoluteMinZ, absoluteMaxX, absoluteMaxY, absoluteMaxZ = tree.get_bounds()
#Update based on query I guess?? seems inefficient but idk
minX = 0 #fips
maxX = 0
minY = 0 #case count
maxY = 0
minZ = 0 #income
maxZ = 0
print(list(tree.intersection((absoluteMinX, absoluteMinY, absoluteMinZ, absoluteMaxX, absoluteMaxY, absoluteMaxZ))))

#From here, can print results based on:
data = pd.read_csv('./processed_data.csv', encoding = "ISO-8859-1")
#Where id == the id of the element found
# data['id'== foundID]
