from openpyxl import load_workbook
import pandas as pd
import plotly.express as px
import plotly.io as pio



# let pandas read dessert spreadsheet
df = pd.read_excel('dessert_research.xlsx')
total = df['dessert'].value_counts()



# print(df['dessert'].hist())
new_df = df['dessert'].value_counts().rename_axis('dessert').reset_index(name='counts')
print(new_df)

# example_fig = px.bar(new_df, x="<col_name>", y="counts", color="counts", title="----------")
# example_fig.show()

dessert_barchart = px.bar(
    data_frame=new_df,
    x='dessert',
    y='counts',
    color='counts',
    opacity=0.9,
    orientation='v',
    barmode='relative',

    labels={'dessert': 'desserts by category'},
    title='Everyones Favourite Dessert',
    width=1000,
    height=700,
    template='gridon'


)

pio.show(dessert_barchart)

# frequency_df = df['frequency'].value_counts().rename_axis('frequency').reset_index(name='counts')
# print(frequency_df)
#
# # example_fig = px.bar(new_df, x="<col_name>", y="counts", color="counts", title="----------")
# # example_fig.show()
#
# frequency_barchart = px.bar(
#     data_frame=frequency_df,
#     x='frequency',
#     y='counts',
#     color='counts',
#     opacity=0.9,
#     orientation='v',
#     barmode='relative',
#
#     labels={'frequency': 'frequency by category'},
#     title='How Often Everyone Has Dessert',
#     width=1000,
#     height=700,
#     template='gridon'
#
#
# )
#
# pio.show(frequency_barchart)
