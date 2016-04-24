
import plotly.plotly as py
import pandas as pd

df_all = pd.read_csv('step3.filteredAll.csv')

df_usa = pd.read_csv('step3.filteredUnitedStates.csv')


df_all['text'] = "ID: " + df_all['Id'].astype(str)
df_usa['text'] = "ID: " + df_usa['Id'].astype(str)

scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
       [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]

trace1 = [dict(
    type='scattergeo',
    lat=df_all['Lat'],
    lon=df_all['Lon'],
    text=df_all['text'],
    mode='markers',
    marker=dict(
        size=3,
        opacity=0.6,
        symbol = 'square',
        reversescale=True,
        autocolorscale=False,
        line=dict(
            width=0.5,
            color='rgba(102, 102, 102)'
        )

    ))]
trace2 = [dict(
    type='scattergeo',
    lat=df_usa['Lat'],
    lon=df_usa['Lon'],
    text=df_usa['text'],
    mode='markers',
    marker=dict(
        size=3,
        opacity=0.6,
        reversescale=True,
        autocolorscale=False,
        line=dict(
            width=0.5,
            color='rgba(0, 0, 0)'
        )

    ))]
data = [trace1,trace2]
layout = dict(

    title='Step3.Visulization',

    geo=dict(
        scope = 'usa',
        projection=dict(type='albers usa'),
        showland=True,
        landcolor="rgb(250, 250, 250)",
        subunitcolor="rgb(217, 217, 217)",
        countrycolor="rgb(217, 217, 217)",
        countrywidth=0.5,
        subunitwidth=0.5
    ),
)

fig = dict(data=trace1, layout=layout)
fig_ = dict(data=trace2, layout=layout)
url = py.plot(fig, validate=False, filename='all')
url = py.plot(fig_, validate=False, filename='usa')
