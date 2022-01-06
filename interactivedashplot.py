import numpy, pandas,  plotly
# generating random data for the graph

data = pandas.DataFrame(numpy.random.randn(100,4),columns='A B C D'.split())

plotly.offline.plot = ([{
    'x': data.index,
    'y': data[col],
    'name': col

} for col in data.columns])
