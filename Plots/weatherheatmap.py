import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Preparing data
data = [go.Heatmap(x=df['day'],
y=df['month'],
z=df['average_max_temp'].values.tolist(),
colorscale='Jet')]
# Preparing layout sepreate data into calendar layout with color intesties as the amount of casses
layout = go.Layout(title='Average Max Temperature', xaxis_title="Day of Week",
yaxis_title="Week of Month")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherheatmap.html')