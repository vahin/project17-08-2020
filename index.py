from pandas import read_csv as rc
from plotly.express import scatter

scatter(rc("pixelMath.csv"), x='student_id', y='level', color="attempt", size='size').show()
