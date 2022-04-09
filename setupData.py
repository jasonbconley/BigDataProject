import os
import pandas as pd
from geopy.geocoders import Nominatim #Needed to get county based on lat and long
geolocator = Nominatim(user_agent="geoapiExercises")

#Loading and Processing CDC Covid data
CDCDataset = pd.read_csv('./CDCDatasetCSVBig.csv', encoding = "ISO-8859-1")
CDCDataFrame = pd.DataFrame(CDCDataset, columns = ['res_state', 'res_county', 'county_fips_code']) #State and County data
JustOhio = CDCDataFrame[CDCDataFrame.res_state == "OH"]
FipCodes = JustOhio.county_fips_code.unique()
#Arrays that will become dataframe later
FipCodesC = []
CountyCountsC = []
CountyNamesC = []
#Get count of each county's covid cases
for county in FipCodes:
    if len(JustOhio[JustOhio.county_fips_code==county].index) > 0:
        CountyCountsC.append(county)
        FipCodesC.append(JustOhio[JustOhio.county_fips_code==county].county_fips_code.count())
        CountyNamesC.append(str(JustOhio[JustOhio.county_fips_code==county].iloc[0].res_county))
    #Replace with code to insert into tree
processedCovidCounts = pd.DataFrame({'county_name': CountyNamesC, 'county_fips': CountyCountsC, 'case_count': FipCodesC})
print(processedCovidCounts)


#Loading and Processing income data
incomeDataset = pd.read_csv('./IncomeDataset.csv', encoding = "ISO-8859-1")
incomeDataFrame = pd.DataFrame(incomeDataset, columns = ['State_ab', 'Lat', 'Lon', 'Mean']) #State, Geo-loc, and Mean-income data
JustOhioInc = incomeDataFrame[incomeDataset.State_ab == "OH"]
for index, row in JustOhioInc.iterrows():
    JustOhioInc.loc[index, 'county_name'] = geolocator.reverse(str(row["Lat"])+","+str(row["Lon"])).raw['address'].get('county').upper().split()[0]
    print(JustOhioInc.loc[index, 'county_name'])
#Code to convert Lat and Lon to a fips code equivalent

CountyNamesInc = JustOhioInc.county_name.unique()
#Arrays that will become data frame later
AverageIncome = []
CountyNamesI = []
#Get average of mean
for county in CountyNamesInc:
    AverageIncome.append(JustOhioInc[JustOhioInc.county_name==county].Mean.mean())
    CountyNamesI.append(str(county))
processedIncomeData = pd.DataFrame({'county_name': CountyNamesI, 'average_income': AverageIncome})
print(processedIncomeData)


#processedIncomeData.set_index('county_name')
#processedCovidCounts.set_index('county_name')
finalData = pd.merge(processedCovidCounts, processedIncomeData, on='county_name', how='inner')
print(finalData)
finalData.to_csv('processed_data.csv')
