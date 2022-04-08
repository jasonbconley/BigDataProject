import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import zipfile

zf = zipfile.ZipFile('CDCDatasetCSV.csv.zip')
df_sample = pd.read_csv(zf.open('CDCDatasetCSV.csv'))

oh_data = df_sample[df_sample['res_state'] == 'OH']

fips = np.unique(oh_data['county_fips_code'].tolist())

firstSum = len(oh_data[(oh_data['county_fips_code'] == fips[0]) & (oh_data['case_month'] == '2021-08')])
secondSum = len(oh_data[(oh_data['county_fips_code'] == fips[1]) & (oh_data['case_month'] == '2021-08')])

print(len(fips))

print("Cases from county (%2d) in August: %2d" % (fips[0], firstSum))
print("Cases from county (%2d) in August: %2d" % (fips[1], secondSum))

#values = np.empty(len(fips), dtype=object)

#i = 0
#for county in fips:
#    values[i] = len(df_sample_r['county_fips_code' == county])
#    ++i

#values = df_sample_r['TOT_POP'].tolist()
#print(values)

#endpts = list(np.mgrid[min(values):max(values):4j])
#colorscale = ["#030512","#1d1d3b","#323268","#3d4b94","#3e6ab0",
#              "#4989bc","#60a7c7","#85c5d3","#b7e0e4","#eafcfd"]
#fig = ff.create_choropleth(
#    fips=fips, values=values, scope=['Ohio'], show_state_data=True,
#    colorscale=colorscale, binning_endpoints=endpts, round_legend_values=True,
#    plot_bgcolor='rgb(229,229,229)',
#    paper_bgcolor='rgb(229,229,229)',
#    legend_title='Population by County',
#    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
#    exponent_format=True,
#)
#fig.layout.template = None
#fig.show()
