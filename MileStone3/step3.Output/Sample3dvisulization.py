

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import math
import plotly.offline as plf
R = 100
def getx(lat,lon):
    lat = math.radians(lat)
    lon = math.radians(lon)
    return R*math.cos(lat)*math.cos(lat)

def gety(lat,lon):
    lat = math.radians(lat)
    lon = math.radians(lon)
    return R*math.cos(lat)*math.sin(lat)

def getz(lat,lon):
    lat = math.radians(lat)
    lon = math.radians(lon)
    return R*math.sin(lat)


datapath = "@2.SyntheticLocationClusters_GreateCircle"
df_cluster1 = pd.read_csv(datapath + "/cluster_0.csv")
df_cluster2 = pd.read_csv(datapath + "/cluster_1.csv")
df_cluster3 = pd.read_csv(datapath + "/cluster_2.csv")
df_cluster4 = pd.read_csv(datapath + "/cluster_3.csv")
df_centers = pd.read_csv(datapath + "/cluster_centers.csv")

df_cluster1["x"] = df_cluster1.apply(lambda x: getx(x['Lat'],x['Lon']),axis=1)
df_cluster1["y"] = df_cluster1.apply(lambda x: gety(x['Lat'],x['Lon']),axis=1)
df_cluster1["z"] = df_cluster1.apply(lambda x: getz(x['Lat'],x['Lon']),axis=1)

df_cluster2["x"] = df_cluster2.apply(lambda x: getx(x['Lat'],x['Lon']),axis=1)
df_cluster2["y"] = df_cluster2.apply(lambda x: gety(x['Lat'],x['Lon']),axis=1)
df_cluster2["z"] = df_cluster2.apply(lambda x: getz(x['Lat'],x['Lon']),axis=1)


df_cluster3["x"] = df_cluster3.apply(lambda x: getx(x['Lat'],x['Lon']),axis=1)
df_cluster3["y"] = df_cluster3.apply(lambda x: gety(x['Lat'],x['Lon']),axis=1)
df_cluster3["z"] = df_cluster3.apply(lambda x: getz(x['Lat'],x['Lon']),axis=1)


df_cluster4["x"] = df_cluster4.apply(lambda x: getx(x['Lat'],x['Lon']),axis=1)
df_cluster4["y"] = df_cluster4.apply(lambda x: gety(x['Lat'],x['Lon']),axis=1)
df_cluster4["z"] = df_cluster4.apply(lambda x: getz(x['Lat'],x['Lon']),axis=1)

df_centers["x"] = df_centers.apply(lambda x: getx(x['Lat'],x['Lon']),axis=1)
df_centers["y"] = df_centers.apply(lambda x: gety(x['Lat'],x['Lon']),axis=1)
df_centers["z"] = df_centers.apply(lambda x: getz(x['Lat'],x['Lon']),axis=1)


print(df_cluster1.head())
print(df_cluster2.head())


trace1 = go.Scatter3d(
    x= df_cluster1['x'],
    y=df_cluster1['y'],
    z=df_cluster1['z'],
    mode='markers',
    marker=dict(
        size=12,
        line=dict(
            color='rgba(217, 217, 217, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)

x2, y2, z2 = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 200).transpose()
trace2 = go.Scatter3d(
    x=df_cluster2['x'],
    y=df_cluster2['y'],
    z=df_cluster2['z'],
    mode='markers',
    marker=dict(
        color='rgb(127, 127, 127)',
        size=4,
        symbol='circle',
        line=dict(
            color='rgb(204, 204, 204)',
            width=1
        ),
        opacity=0.9
    )
)

layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=[trace1], layout=layout)
plf.plot(fig, filename='simple-3d-scatter')
