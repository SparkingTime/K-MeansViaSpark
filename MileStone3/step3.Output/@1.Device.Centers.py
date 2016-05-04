
import plotly.plotly as py
import pandas as pd



df_centers_euclidean = pd.read_csv(
    './@1.DeviceLocationDataClusters_Euclidian/cluster_centers.csv')
df_centers_greatecircle = pd.read_csv(
    './@1.DeviceLocationDataClusters_GreateCircle/cluster_centers.csv')



df_cluster1 = df_cluster1.sample(frac=0.01, replace=True)
df_cluster2 = df_cluster2.sample(frac=0.01, replace=True)
df_cluster3 = df_cluster3.sample(frac=0.01, replace=True)
df_cluster4 = df_cluster4.sample(frac=0.01, replace=True)
df_cluster5 = df_cluster5.sample(frac=0.01, replace=True)
scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
       [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]


trace1 = [dict(
    type='scattergeo',
    lat=df_centers['Lat'],
    lon=df_centers['Lon'],
    text=df_centers['Id'],
    mode='markers',
    marker=dict(
        size=8,
        symbol='star-diamond-dot',
        reversescale=True,
        autocolorscale=False,
        color=u'rgb(218,165,32)',
        line=dict(
            width=0.5,
            color=u'rgb(218,165,32)'
        )

    ))]

trace2 = [dict(
    type='scattergeo',
    lat=df_centers['Lat'],
    lon=df_centers['Lon'],
    text=df_centers['Id'],
    mode='markers',
    marker=dict(
        size=8,
        symbol='star-diamond-dot',
        reversescale=True,
        autocolorscale=False,
        color=u'rgb(218,165,32)',
        line=dict(
            width=0.5,
            color=u'rgb(218,165,32)'
        )

    ))]
layout = dict(

    title='Step3.Visulization',

    geo=dict(

        scope='usa',
        projection=dict(type='albers usa'),
        showland=True,
        landcolor="rgb(250, 250, 250)",
        subunitcolor="rgb(217, 217, 217)",
        countrycolor="rgb(217, 217, 217)",
        countrywidth=0.5,
        subunitwidth=0.5
    ),
)

#fig = dict(data=trace1, layout=layout)
#fig_ = dict(data=trace2, layout=layout)
fig = dict(data=trace1 + trace2 + trace3 +
           trace4 + trace5 + trace6, layout=layout)
#url = py.plot(fig_wtf, validate=False, filename='all')
#url = py.plot(fig, validate=False, filename='all')
#url = py.plot(fig_, validate=False, filename='usa')
url = py.plot(fig, validate=False, filename='@1.DeviceStatus_Euclidian')
