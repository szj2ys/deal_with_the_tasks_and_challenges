
pandas 画图
```python
df.plot.area     df.plot.barh     df.plot.density  df.plot.hist     df.plot.line     df.plot.scatter
df.plot.bar      df.plot.box      df.plot.hexbin   df.plot.kde      df.plot.pie
```

## All in one, altair
```python
alt.Chart(stocks).mark_circle().encode(
    x=alt.X('date:T',title=None),
    y=alt.Y('price:Q',title='The price'),
    color=alt.Color('symbol:N', title='Symbol')
).configure_axisX(
    labelAngle=45
).properties(
    title='Stocks price',
    width=800
)
```








