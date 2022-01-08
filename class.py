import pandas as pd
import plotly_express as px

df = pd.read_csv("cc.csv")

fig = px.scatter(df, x="Date", y="Cases", color="Country", title='cc')

fig.show()
