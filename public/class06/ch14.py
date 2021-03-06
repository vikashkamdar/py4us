# ch14.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#grouping

# Groups in the data may be visually grouped using the group parameter:

from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Bar(df, label='yr', values='mpg', agg='median', group='origin',
        title="Median MPG by YR, grouped by ORIGIN", legend='top_right')

output_file("/tmp/ch14.html")

show(p)
# What is origin?
print(df[['name','origin']].head(33))
print(df[['name','origin']].tail(33))

