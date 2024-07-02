import csv
from datetime import datetime
# from plotly.graph_objs import Layout
# from plotly import offline

file_name_1 = 'world_fires_1_day.csv'
file_name_2 = 'world_fires_7_day.csv'

data1, data2 = [], []

with open(file_name_1, 'r') as f:
    reader1 = csv.reader(f)
    header1 = next(reader1)

    for row in reader1:
        if len(row) > 5:
            date = datetime.strptime(row[5], '%Y-%m-%d')
            data1.append(str(row[7]))
            data2.append(date)

data_1, data_2 = [], []

with open(file_name_2, 'r') as f2:
    reader2 = csv.reader(f2)
    header2 = next(reader2)

    for row in reader2:
        if len(row) > 5:
            date = datetime.strptime(row[5], '%Y-%m-%d')
            data_1.append(str(row[7]))
            data_2.append(date)
#
# layout = Layout(title='World Fires Map', geo=dict(showland=True))
#
# data = [
#     {
#         'type': 'scattergeo',
#         # 'lon': longitude,
#         # 'lat': latitude,
#         'marker': {
#             'color': 'red',
#         },
#     }
# ]
#
# fig = {'data': data, 'layout': layout}
#
# offline.plot(fig, filename='world_fires_map.html')

