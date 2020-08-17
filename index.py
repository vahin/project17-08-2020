from pandas import read_csv as rc
from plotly.express import scatter

df = rc("pixelMath.csv")
fig = scatter(df, x='student_id', y='level', color="attempt", size='size')
fig.show()
