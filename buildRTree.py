import os
import pandas as pd
from rtree import index #Requires 'pip install rtree'


data = pd.read_csv('./processed_data.csv', encoding = "ISO-8859-1")

#set up properties to it can be 3d
prop = index.Property()
prop.dimension = 3
prop.dat_extension = 'data'
prop.idx_extension = 'index'
prop.overwrite = True #Not working, don't know why
#establish tree and ranges
tree = index.Index('covid_data', properties=prop)
counter = 0
for index, row in data.iterrows():
    tree.insert(row['id'], coordinates=(int(row['county_fips']), row['case_count'], row['average_income'], row['county_fips'], row['case_count'], row['average_income']))
tree.close()
