#!/usr/local/bin/python2.7

import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

df_all = pd.read_csv('./step3.filteredInputData/step3.filteredAll.csv')
df_usa = pd.read_csv('./step3.filteredInputData/step3.filteredUnitedStates.csv')

df_all = df_all[~df_all['Id'].isin(df_usa['Id'])]

fig = plt.figure(figsize=(20,20))
map = Basemap(projection='gall',
              resolution='f',
              area_thresh=1000.0,
              lat_0=0,lon_0=0)

map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='#888888')
map.drawmapboundary(fill_color='#f4f4f4')




x,y = map(df_usa['Lon'].values, df_usa['Lat'].values)
map.plot(x, y, 'y.', markersize=.9)
x,y = map(df_all['Lon'].values, df_all['Lat'].values)
map.plot(x, y, 'r.', markersize=.9)
#plt.savefig('box.png',bbox_inches='tight')
plt.show()

