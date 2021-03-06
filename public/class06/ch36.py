# ch36.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#userguide-charts-scatter-marker

# As with color, the marker parameter can be given a column name to
# group by the values of that column, using a different marker shape
# for each group:

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='displ', y='hp', marker='cyl',
            title="HP vs DISPL (marked by CYL)", legend="top_left",
            xlabel="Displacement", ylabel="Horsepower")

output_file("/tmp/ch36.html")

show(p)


