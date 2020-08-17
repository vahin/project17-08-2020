import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("pixelMath.csv")
fig = px.scatter(df, x='student_id', y='level', color="attempt", size='size')
fig.show()
