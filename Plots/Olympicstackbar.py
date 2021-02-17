import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Sorting values and select 20 first value
new_df = df.sort_values(by=['Total'],
ascending = [False]).head(20).reset_index()
# Preparing data
# Create bars for each country, one for deaths, recoveries, and deaths the stack bars based on data per country
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze Medal',
marker = {'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver Medal',
marker = {'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold Medal',
marker = {'color': '#FFD700'})
data = [trace1, trace2, trace3]
# Preparing layout
layout = go.Layout(title='Olympic Medal Earn By Countries during Rio Olympics 2016', xaxis_title= "Country" ,
yaxis_title = "Number Medals", barmode='stack')
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Olympicstackbarchart.html')