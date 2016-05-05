
import plotly.plotly as py
import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("Dmethod", help=" name of jar file", type=str)
args = parser.parse_args()
method = args.Dmethod

datapath = "@2.SyntheticLocationClusters_" + method
df_cluster1 = pd.read_csv(datapath + "/cluster_0.csv")
df_cluster2 = pd.read_csv(datapath + "/cluster_1.csv")
df_cluster3 = pd.read_csv(datapath + "/cluster_2.csv")
df_cluster4 = pd.read_csv(datapath + "/cluster_3.csv")
df_centers = pd.read_csv(datapath + "/cluster_centers.csv")
df_centers1 = pd.read_csv(
    "@2.SyntheticLocationClusters_Euclidean/cluster_centers.csv")

df_centers2 = pd.read_csv(
    "@2.SyntheticLocationClusters_GreateCircle/cluster_centers.csv")

#df_all['text'] = df_all['Id'].astype('U')
#df_usa['text'] = df_usa['Id'].astype('U')

scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
       [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]

trace_center1 = [dict(
    type='scattergeo',
    lat=df_centers1['Lat'],
    lon=df_centers1['Lon'],
    # text=df_all['Id'],
    mode='markers',
    marker=dict(
        size=10,

        reversescale=True,
        autocolorscale=False,
        color=u'rgb(200,100,32)',
        line=dict(
            width=0.9,
            color=u'rgb(218,165,32)'
        )

    ))]

trace_center2 = [dict(
        type='scattergeo',
        lat=df_centers2['Lat'],
        lon=df_centers2['Lon'],
        # text=df_all['Id'],
        mode='markers',
        marker=dict(
            size=12,
            symbol='star-diamond-dot',
            reversescale=True,
            autocolorscale=False,
            color=u'rgb(218,165,32)',
            line=dict(
                width=0.9,
                color=u'rgb(218,165,32)'
            )

    ))]

trace1 = [dict(
    type='scattergeo',
    lat=df_cluster1['Lat'],
    lon=df_cluster1['Lon'],
    # text=df_all['Id'],
    mode='markers',
    marker=dict(
        size=3,
        opacity=0.5,
        reversescale=True,
        autocolorscale=False,
        color=u'rgb(255, 0, 0)',
        line=dict(
            width=0.5,
            color=u'rgb(255, 0, 0)'
        )

    ))]
trace2 = [dict(
    type='scattergeo',
    lat=df_cluster2['Lat'],
    lon=df_cluster2['Lon'],
    # text=df_usa['Id'],
    mode='markers',
    marker=dict(
        size=3,
        opacity=0.5,
        reversescale=True,
        autocolorscale=False,
        color=u'rgb(0, 0, 255)',
        line=dict(
            width=0.5,
            color=u'rgb(0, 0, 255)'
        )

    ))]

trace3 = [dict(
    type='scattergeo',
    lat=df_cluster3['Lat'],
    lon=df_cluster3['Lon'],
    # text=df_all['Id'],
    mode='markers',
    marker=dict(
        size=3,
        opacity=0.5,
        symbol='square',
        reversescale=True,
        autocolorscale=False,
        color=u'rgb(0, 0, 0)',
        line=dict(
            width=0.5,
            color=u'rgb(0, 0, 0)'
        )

    ))]
trace4 = [dict(
    type='scattergeo',
    lat=df_cluster4['Lat'],
    lon=df_cluster4['Lon'],
    # text=df_all['Id'],
    mode='markers',
    marker=dict(
        size=3,
        opacity=0.5,
        reversescale=True,
        autocolorscale=False,
        color=u'rgb(102, 102, 102)',
        line=dict(
            width=0.5,
            color=u'rgb(102, 102, 102)'
        )

    ))]

trace5 = [dict(
    type='scattergeo',
    lat=df_centers['Lat'],
    lon=df_centers['Lon'],
    # text=df_all['Id'],
    mode='markers',
    marker=dict(
        size=12,
        symbol='star-diamond-dot',
        reversescale=True,
        autocolorscale=False,
        color=u'rgb(218,165,32)',
        line=dict(
            width=0.9,
            color=u'rgb(218,100,32)'
        )

    ))]

layout = dict(

    title='SyntheticLocation Clustering via ' + method,

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

layout_center = dict(

    title='SyntheticLocation Clustering centers Comparision Euclidean vs GreatCircle' ,

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
fig = dict(data=trace1 + trace2 + trace3 + trace4 + trace5, layout=layout)
fig1 = dict(data= trace_center1 +trace_center2, layout=layout_center)
#url = py.plot(fig_wtf, validate=False, filename='all')
#url = py.plot(fig, validate=False, filename='all')
#url = py.plot(fig_, validate=False, filename='usa')

url = py.plot(fig, validate=False, filename='SampleGeoClustering_'+method)
url = py.plot(fig1, validate=False, filename='SampleGeoClustering_Cluster_Centers')
