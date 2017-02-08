# ch20.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#whisker-color

# The color of the whiskers can be similarly controlled using the whisker_color parameter. For a single color:

from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = BoxPlot(df, values='mpg', label='cyl', whisker_color='goldenrod',
            title="MPG Summary (grouped by CYL, shaded whiskers)")

output_file("boxplot.html")

show(p)

