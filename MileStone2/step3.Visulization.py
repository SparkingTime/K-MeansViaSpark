
import plotly.plotly as py
import pandas as pd

df_all = pd.read_csv('./step3.filteredInputData/step3.filteredAll.csv')

df_usa = pd.read_csv('./step3.filteredInputData/step3.filteredUnitedStates.csv')

df_all = df_all.sample(frac=0.01, replace=True)
df_usa = df_usa.sample(frac=0.01, replace=True)

#df_all['text'] = df_all['Id'].astype('U')
#df_usa['text'] = df_usa['Id'].astype('U')

scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
       [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]

trace1 = [dict(
    type='scattergeo',
    lat=df_all['Lat'],
    lon=df_all['Lon'],
    #text=df_all['Id'],
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
    #text=df_usa['I'],
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

        projection=dict(type='orthographic'),
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
fig_wtf = dict(data = trace1+trace2,layout=layout)
url = py.plot(fig_wtf, validate=False, filename='all vs usa')
#url = py.plot(fig, validate=False, filename='all')
#url = py.plot(fig_, validate=False, filename='usa')
