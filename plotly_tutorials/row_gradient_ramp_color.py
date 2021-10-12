# *_*coding:utf-8 *_*
import plotly.graph_objects as go
import pathlib
import pandas as pd

colors = [
    'rgb(239, 243, 255)',  # rgb值越接近255，越接近白色
    'rgb(189, 215, 231)',
    'rgb(107, 174, 214)',
    'rgb(59, 130, 189)',
    'rgb(9, 81, 156)'
]

data = {'Year': [2015, 2016, 2017, 2018, 2019], 'Color': colors}

df = pd.DataFrame(data)

print(df)

fig = go.Figure(data=[
    go.Table(
        # 表头
        header=dict(
            values=["Color", "<b>YEAR</b>"],  # 表头名称
            line_color='white',
            fill_color='white',
            align='center',
            font=dict(color='black', size=12)),

        # 单元格
        cells=dict(
            values=[df.Color, df.Year],  # 两个列属性
            line_color=[df.Color],
            fill_color=[df.Color],
            align='center',
            font=dict(color='black', size=13)))
])

fig.write_image(pathlib.Path(__file__).stem + '.png')
