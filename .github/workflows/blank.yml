import csv
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

df = pd.read_csv('sales.csv')
print(df)

barchart = px.bar(
    data_frame=df,
    x='month',
    y='sales',
    color='sales',
    opacity=0.9,
    orientation='v',
    barmode='relative',

    labels={'month': 'year of sales'},
    title='Sales By Month',
    width=1000,
    height=700,
    template='gridon'


)

pio.show(barchart)
