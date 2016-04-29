
import plotly.plotly as py
import pandas as pd

df = pd.read_csv('step2.sample_geo.csv')
df.head()

df['text'] = "ID: " + df['LocationID'].astype(str)


scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
       [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]

data = [dict(
    type='scattergeo',
    lat=df['Latitude'],
    lon=df['Longitude'],
    text=df['text'],
    mode='markers',
    marker=dict(
        size=3,
        opacity=0.6,
        reversescale=True,
        autocolorscale=False,
        line=dict(
            width=0.5,
            color='rgba(102, 102, 102)'
        )

    ))]

layout = dict(
        scope='usa',
        title = 'Sample Geo Data Visulization',

        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

fig = dict(data=data, layout=layout)
url = py.plot(fig, validate=False, filename='d3-airports')
