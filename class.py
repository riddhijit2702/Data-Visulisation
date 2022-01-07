import pandas as pd
import plotly_express as px

df = pd.read_csv("cc.csv")

fig = px.line(df, x="Date", y="No. of cases everyday", color="Country", title='Covid Report')

fig.show()