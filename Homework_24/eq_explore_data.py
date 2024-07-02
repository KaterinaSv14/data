import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline
from plotly import colors

print(colors.PLOTLY_SCALES.keys())

with open('../../pythonProject1/Homework_24/2_1.json', 'r') as f:
    values = json.load(f)

all_eq_dicts = values['features']
# print(len(all_eq_dicts))
mags, lons, lats, hover_text = [], [], [], []
for eq in all_eq_dicts:
    mags.append(eq['properties']['mag'])
    lons.append(eq['geometry']['coordinates'][0])
    lats.append(eq['geometry']['coordinates'][1])
    hover_text.append(eq['properties']['title'])

data = [Scattergeo(lon=lons, lat=lats)]
layout = Layout(title=values['metadata']['title'])

data = [
  {
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
      #'size': [mag * 5 for mag in mags],
      'color': mags,
      'colorscale': 'Viridis',
      'reversescale': True,
      'colorbar': {'title': 'Magnitude'},
    }
  }
]

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='data/global_earthquakes.html')

